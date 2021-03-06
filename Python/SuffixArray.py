#!/usr/bin/env python3

ALPHABET = [chr(i) for i in range(32,128)]
ALPHABET.insert(0, "\n"); ALPHABET.insert(1, "\t"); ALPHABET.insert(2, "\r")
ALPHABET.insert(0, ALPHABET.pop(ALPHABET.index("$")))
for i in range(10): ALPHABET.remove(str(i))
POS = {c : p for (p, c) in enumerate(ALPHABET)}

class SaStrOrder(str):
    
    def __init__(self, text, *args):
        super().__init__()
        
    def __lt__(self, other):
        for i in range(min(len(self), len(other))):
            a = POS.get(self[i])
            b = POS.get(other[i])
            if a != b:
                return a < b
        return len(self) < len(other)

class SuffixArray(list):
    
    def __init__(self, text = None, trie = None):
        
        super().__init__()
        
        if text:
            if text[-1] != "$": text += "$"
            pairs = list()
            for index in range(len(text)):
                pairs.append((index, SaStrOrder(text[index:])))
            pairs.sort(key = lambda x : x[1])
            self.extend([i for (i, _) in pairs])
        elif not text and trie:
            self.from_trie(trie)
        else:
            raise TypeError("SuffixArray __init__() takes at least one argument: text (a string) or trie")
        
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
        
        if text[-1] != "$": text += "$"
        
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
