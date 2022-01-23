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
    
    def search_pattern(self, text, pos = None):
        
        occurrences = []
        
        if pos is None:
            for pos in range(len(text)):
                occs = self.search_pattern(text, pos = pos)
                for occ in occs:
                    occurrences.append((pos, occ))
            return occurrences
        else:
            if hasattr(self, "index"):
                occurrences.extend(self.index)
            if pos >= len(text):
                return occurrences
            for child in self.children:
                if child.name == text[pos]:
                    occs = child.search_pattern(text, pos = pos+1)
                    occurrences.extend(occs)
            return occurrences

            
                
                
            
        
    

