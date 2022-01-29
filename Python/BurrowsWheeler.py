#!/usr/bin/env python3

import SuffixArray as sa

class BurrowsWheeler(str):
    
    def __new__(self, text, suffix_array = None):
        
        if text[-1] != "$": text += "$"

        if not suffix_array:
            suffix_array = sa.SuffixArray(text = text)
        bwt = str()
        for idx in suffix_array:
            bwt += text[idx-1]
        
        return str.__new__(self, bwt)
#        return sa.SaStrOrder.__new__(self, bwt)
        
    

