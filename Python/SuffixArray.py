#!/usr/bin/env python3

import Trie

class SuffixArray(list):
    
    def __init__(self, text):
        
        super().__init__()
        trie = Trie.SuffixTree(text)
        self.from_trie(trie)
        
    def from_trie(self, trie):
            
        children = trie.children
        
        if children:
            for child in children:
                self.from_trie(child)
        else:
            self.extend(trie.index)

    def pattern_search(self, text, pattern):
        """
        Find occurrences of a pattern in a text.
        Input:
            suffixarray: a suffix array
            text: a string
            pattern : a string
        Output:
            list of positions where the pattern occurs
        """
        
        start = 0
        end = len(self)
        
        def narrow_start(idx, letter):
            for j in range(start, end):
                if text[self[j] + idx] == letter:
                    return j
            return end
    
        def narrow_end(idx, letter):
            for j in reversed(range(start, end)):
                if text[self[j] + idx] == letter:
                    return j+1
            return start
    
        for idx, c in enumerate(pattern):
            start = narrow_start(idx, c)
            end   = narrow_end(idx, c)

        if start >= end:
            return None
        
        return sorted(self[start:end])

    def to_bwt(self, text):
        """
        Construct the Burrows Wheeler transform (BWT)
        Input:
            text: a string
        Output:
            the BW-transformation (a string)
        """
    
        bwt = str()
        
        for i in range(len(self)):
            bwt += text[self[i] - 1]
    
        return bwt

def bwt_search(bwt, text, pattern):
    """
    Find occurrences of a pattern in a text.
    Input:
        bwt: a BW-transformer (string)
        text: a string
        pattern: a string
    Output:
        list of positions where the pattern occurs
    """
    
    return None
    
    
    
    