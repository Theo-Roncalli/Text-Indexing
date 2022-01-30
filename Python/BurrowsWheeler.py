#!/usr/bin/env python3

import SuffixArray as sa

class BurrowsWheeler():
    
    def __init__(self, text, suffix_array = None, compression = None):
        
        if text[-1] != "$": text += "$"

        if not suffix_array:
            suffix_array = sa.SuffixArray(text = text)
        self.bwt = str()
        for idx in suffix_array:
            self.bwt += text[idx-1]
        
        if not compression:
            self.compression = False
        else:
            self.compression = True
            self.compress()
    
    def __str__(self):
        return self.bwt
    
    def compress(self, encode="run-length"):
        
        if self.compression is True:
            raise ValueError("The bw-transform is already compressed.")
        elif encode == "run-length":
            bwt = ""
            last_letter = None
            count = 1
        for letter in self.bwt:
            if letter == last_letter:
                count += 1
            elif letter != last_letter and count > 1:
                bwt += (str(count) + letter)
                last_letter = letter
                count = 1
            elif letter != last_letter and count == 1:
                bwt += letter
                last_letter = letter
        if count > 1:
            bwt += str(count)
        self.bwt = bwt
        
        
            
