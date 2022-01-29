#!/usr/bin/env python3

import SuffixArray

class BurrowsWheeler(str):
    
    def __new__(cls, text, sa = None):

        if not sa:
            sa = SuffixArray.SuffixArray(text)
        bwt = str()
        for idx in sa:
            bwt += text[idx-1]

        obj = str.__new__(cls, bwt)
        return obj
    
    """
    def __init__(self, text, sa = None):
        
        if not sa:
            sa = SuffixArray.SuffixArray(text)
            
        bwt = str()
        for idx in sa:
            bwt += text[idx-1]
        
        self.text = text
        self.bwt = bwt
        """        
        
        
        
        
