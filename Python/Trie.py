#!/usr/bin/env python3

from ete3 import Tree

class Trie(Tree):
    
    def __init__(self, name = None, words = None):
        
        if name:
            super().__init__(name = name)
        else:
            super().__init__()
        
        self.max_index = 0
        
        if words:
            for index, word in enumerate(words):
                self.insert(word, index)
            self.max_index = index
    
    def __str__(self):
        return self.get_ascii(show_internal = True, attributes=["name", "index"])
    
    def add(self, words):
        """
        Construct a trie from a list of words.
        Input:
            words: a list of strings
        Output:
            trie containing the words, annotated with the words indices
        """
        
        index = self.max_index
        for word in words:
            index += 1
            self.insert(word, index)
        self.max_index = index
    
    def insert(self, word, index):
        """
        Insert word in a trie and add its index.
        Input:
            trie: a trie (ete3.Tree)
            word: a string
            index: an integer corresponding to the word index
        Result:
            Modifies input trie. It inserts new branches in alphabetical order
        """
    
        if word:
            c = word[0]
            pos = -1
            for i, child in enumerate(self.children):
                if child.name >= c:
                    pos = i
                    break
            
            if pos == -1:
                child = Trie(name = c)
                self.children.append(child)
            elif child.name != c:
                child = Trie(name = c)
                self.children.insert(pos, child)
            else:
                child = self.children[pos]
            
            child.insert(word[1:], index)
    
        else:
            if hasattr(self, "index"):
                self.index.append(index)
            else:
                self.add_features(index = [index])
    
    def pattern_search(self, text, pos = None):
        """
        Find occurrences of multiple patterns.
        Input:
            text : a string
            pos : an integer, optional
            For searching patterns at a specific position in text. The default is None.
        Output:
            list of paired tuple (pos, pattern)
        """
        
        if pos is None:
            occurrences = list()
            for pos in range(len(text)):
                patterns = self.pattern_search(text, pos = pos)
                for pattern in patterns:
                    occurrences.append((pos, pattern))
            return occurrences
        else:
            patterns = list()
            if hasattr(self, "index"):
                patterns.extend(self.index)
            if pos >= len(text):
                return patterns
            for child in self.children:
                if child.name == text[pos]:
                    patt = child.pattern_search(text, pos = pos+1)
                    patterns.extend(patt)
            return patterns

class SuffixTree(Trie):
    
    def __init__(self, text = None, name = None, compression = False):
        
        if name:
            super().__init__(name = name)
        else:
            super().__init__()
        
        if text:
            for pos in range(len(text)):
                suffix = text[pos:]
                self.insert(suffix, pos)
        
        if compression is True:
            self.compressed = True
            self.compress()
        else:
            self.compressed = False
    
    def insert(self, word, index):
    
        if word:
            c = word[0]
            pos = -1
            for i, child in enumerate(self.children):
                if child.name >= c:
                    pos = i
                    break
        
            if pos == -1:
                child = SuffixTree(name = c)
                self.children.append(child)
            elif child.name != c:
                child = SuffixTree(name = c)
                self.children.insert(pos, child)
            else:
                child = self.children[pos]
        
            child.insert(word[1:], index)

        else:
            if hasattr(self, "index"):
                self.index.append(index)
            else:
                self.add_features(index = [index])
    
    def compress(self):

        def compression(self):
                
            children = self.children
        
            for child in children:
                child.compress()
                
            if len(children) == 1:
                self.name += child.name
                if hasattr(child, "index"):
                    if hasattr(self, "index"):
                        self.index.extend(child.index)
                    else:
                        self.index = child.index
                self.children = child.children
        
        self.compressed = True
        compression(self)
    
    def pattern_search(self, pattern):
        
        if self.compressed is False:
            occs = list()
            if pattern:
                c = pattern[0]        
                for child in self.children:
                    if child.name == c:
                        occs = child.pattern_search(pattern[1:])
                        break
            else:
                for leaves in self.get_leaves():
                    occs.extend(leaves.index)
            return sorted(occs)
        
        else:

            def lcp_length(child_name, pattern):
                # Compute the longest common prefix (lcp) length between the child name and the pattern
                for i, (c1, c2) in enumerate(zip(child_name, pattern)):
                    if c1 != c2:
                        return i
                return i+1
    
            for child in self.children:
                lcp = lcp_length(child.name, pattern)
                
                if lcp == len(pattern):
                    occs = list()
                    for leaves in child.get_leaves():
                        occs.extend(leaves.index)
                    return occs
                elif lcp == len(child.name):
                    return sorted(child.pattern_search(pattern[lcp:]))
            return list()
