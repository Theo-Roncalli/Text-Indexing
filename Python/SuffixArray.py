#!/usr/bin/env python3

ALPHABET = [chr(i) for i in range(128)]
ALPHABET.insert(0, ALPHABET.pop(ALPHABET.index("$")))
POS = {c : p for (p, c) in enumerate(ALPHABET)}

class SaStrOrder:
    def __init__(self, inner):
        self.inner = inner
        
    def __str__(self):
        return self.inner

    def __lt__(self, other):
        for i in range(min(len(self.inner), len(other.inner))):
            a = POS.get(self.inner[i])
            b = POS.get(other.inner[i])
            if a != b:
                return a < b
        return len(self.inner) < len(other.inner)

class SuffixArray(list):
    
    def __init__(self, text = None, trie = None):
        
        super().__init__()
        
        if text:
            pairs = list()
            for index in range(len(text)):
                pairs.append((index, text[index:]))
            pairs.sort(key = lambda x : x[1])
            self.extend([i for (i, _) in pairs])
        elif not text and trie:
            self.from_trie(trie)
        else:
            raise TypeError("SuffixArray __init__() takes at lease one argument: text (a string) or trie")
        
    def from_trie(self, trie):
            
            children = trie.children
            
            if children:
                for child in children:
                    self.from_trie(child)
            else:
                self.extend(trie.index)
