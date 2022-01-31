#!/usr/bin/env python3

ALPHABET = [chr(i) for i in range(128)]
ALPHABET.insert(0, ALPHABET.pop(ALPHABET.index("$")))
for i in range(0,10): ALPHABET.remove(str(i))
POS = {c : p for (p, c) in enumerate(ALPHABET)}

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
            self.compression = None
        else:
            self.compression = "run-length"
            self.compress()
    
    def __str__(self):
        return self.bwt
    
    def compress(self, encode="run-length"):
        
        if self.compression:
            raise ValueError("The bw-transform is already compressed.")
        
        if encode == "run-length":
            self.compression = "run-length"
            bwt = ""
            last_letter = None
            count = 1
            for letter in self.bwt:
                if letter == last_letter:
                    count += 1
                elif count == 1:
                    bwt += letter
                    last_letter = letter
                elif count > 1:
                    bwt += (str(count) + letter)
                    last_letter = letter
                    count = 1

            if count > 1:
                bwt += str(count)
            self.bwt = bwt
    
    def decompress(self):
        
        if not self.compression:
            raise ValueError("The bw-transform is already decompressed.")
        
        if self.compression == "run-length":
            self.compression = None
            bwt = ""
            last_letter = None
            count = 0
            for letter in self.bwt:
                if not letter.isdigit():
                    if count != 0:
                        bwt = bwt + last_letter * (count-1)
                        count = 0
                    last_letter = letter
                    bwt += letter
                else:
                    count = count*10 + int(letter)
            if count != 0: bwt = bwt + last_letter * (count-1)
            self.bwt = bwt
    
    def toString(self):
        """
        Implement decompression of a run-length encoding bwt text.
        """
        
        def compute_first_column(occs):
            F = {}
            totc = 1
            F["$"] = (0, 1)
            del occs["$"]
            for letter in sorted(occs.keys()):
                count = occs[letter]
                F[letter] = (totc, totc + count)
                totc += count
            return F

        def rank(bwt):
            occs = dict()
            ranks = []
            for letter in bwt:
                if letter not in occs:
                    occs[letter] = 0
                ranks.append(occs[letter])
                occs[letter] += 1
            return ranks, occs
        
        bwt = list(self.bwt)
        ranks, occs = rank(bwt)
        F = compute_first_column(occs)
        text = "$"
        row = 0
    
        while bwt[row] != "$":
            letter = bwt[row]
            text = letter + text
            row = F[letter][0] + ranks[row]
        
        return text

    def count(self):
        """
        Returns an array of length of the alphabet such that the i-th element corresponds
        to the number of symbols smaller than the i-th symbol in the lexigraphical order.
        """
        
        counts = dict()
        counts[ALPHABET[0]] = 0
        last_letter = ALPHABET[0]
        
        for letter in ALPHABET[1:]:
            counts[letter] = counts[last_letter] + self.bwt.count(last_letter)
            last_letter = letter
        
        return counts
    
    def occ(self, letter, pos):
        """
        Returns the number of occurrences of a letter in the text prefix [0:pos-1].
        """
        
        return self.bwt[:pos].count(letter)
    
    def ltf_mapping(self, index, counts = None):
        """
        Performs last-to-first column mapping.
        """
        
        if counts is None:
            counts = self.count()
        
        letter = self.bwt[index]
        
        return counts[letter] + self.occ(letter, index)
        
        
        