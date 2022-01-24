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
                self.children.append(Trie(name = c))
            elif child.name != c:
                self.children.insert(pos, Trie(name = c))
            
            self.children[pos].insert(word[1:], index)
    
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
            occurrences = []
            for pos in range(len(text)):
                patterns = self.pattern_search(text, pos = pos)
                for pattern in patterns:
                    occurrences.append((pos, pattern))
            return occurrences
        else:
            patterns = []
            if hasattr(self, "index"):
                patterns.extend(self.index)
            if pos >= len(text):
                return patterns
            for child in self.children:
                if child.name == text[pos]:
                    patt = child.pattern_search(text, pos = pos+1)
                    patterns.extend(patt)
            return patterns

class Suffix_tree(Trie):
    
    def __init__(self, text = None):
        
        super().__init__()
        
        if text:
            for pos in range(len(text)):
                suffix = text[pos:]
                self.insert(suffix, pos)

