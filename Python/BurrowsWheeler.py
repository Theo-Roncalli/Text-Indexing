#!/usr/bin/env python3

ALPHABET = [chr(i) for i in range(32,128)]
ALPHABET.insert(0, "\n"); ALPHABET.insert(1, "\t"); ALPHABET.insert(2, "\r")
ALPHABET.insert(0, ALPHABET.pop(ALPHABET.index("$")))
for i in range(10): ALPHABET.remove(str(i))
POS = {c : p for (p, c) in enumerate(ALPHABET)}
NEXT_LETTER = {ALPHABET[i]: ALPHABET[i+1] for i in range(len(ALPHABET) - 1)}

import SuffixArray as sa

class BurrowsWheeler():
    
    def __init__(self, text, suffix_array = None, compression = None, occs = True, step = 50):

        if occs not in [True, False]:
            raise ValueError("\"occs\" argument must take a boolean value.")
        
        def counts(self):
            """
            Returns an array of length of the alphabet such that the i-th element corresponds
            to the number of symbols smaller than the i-th symbol in the lexigraphical order.
            """
            
            self.counts = dict()
            self.counts[ALPHABET[0]] = 0
            last_letter = ALPHABET[0]
            
            for letter in ALPHABET[1:]:
                self.counts[letter] = self.counts[last_letter] + self.bwt.count(last_letter)
                last_letter = letter
        
        if text[-1] != "$": text += "$"

        if not suffix_array:
            suffix_array = sa.SuffixArray(text = text)
        self.bwt = str()
        self.mark = dict()
        for idx_bwt, idx_sa in enumerate(suffix_array):
            self.bwt += text[idx_sa-1]
            self.mark[idx_bwt] = idx_sa
        
        counts(self)        
        
        if occs is True:
            self.occurrence_count()
        
        if not compression:
            self.compression = None
        else:
            self.compression = "run-length"
            self.compress()
        
    def __str__(self):
        return self.bwt
    
    def __len__(self):
        return len(self.bwt)
    
    def compress(self, encode="run-length"):
        
        if self.compression:
            raise ValueError("The bw-transformation is already compressed.")
        
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
            raise ValueError("The bw-transformation is already decompressed.")
        
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
    
    def toString(self, option = "classic"):
        """
        Implement decompression of a run-length encoding bwt text.
        """
        
        if self.compression is not None:
            raise ValueError("The bw-transformation must be decompressed before.")
        
        if option == "classic":
            
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
        
        elif option == "Ferragina":
            
            LastToFirst = self.ltf_mapping(1)
            text = self.bwt[0] + "$"
            
            for _ in range(len(self.bwt) - 3):
                letter = self.bwt[LastToFirst]
                text = letter + text
                LastToFirst = self.ltf_mapping(LastToFirst)
                
            return text
    
    def occurrence_count(self):
        """
        Add attribute "occs", which is a dictionary containing lists of same length as bw-transform.
        These lists contains, for each index i, the number of occurrences of a letter in the text prefix [0:pos].
        """
        
        if hasattr(self, "occs"):
            raise AttributeError("The bw-transformation object contains already the \"occs\" attribute.")
        
        self.occs = {letter: list() for letter in ALPHABET}
        for letter in ALPHABET:
            n = 0
            for i in range(len(self.bwt)):
                if self.bwt[i] == letter:
                    n += 1
                self.occs[letter].append(n)
    
    def ltf_mapping(self, index):
        """
        Performs last-to-first column mapping.
        """
        
        letter = self.bwt[index]
        return self.counts[letter] + self.occs[letter][index] - 1
    
    def backward_search(self, pattern):
        
        if not hasattr(self, "occs"):
            raise AttributeError("The attribute \"occs\" must be computed before using indexing.")
        elif self.compression is not None:
            raise ValueError("The bw-transformation must be decompressed before.")
                    
        letter = pattern[len(pattern) - 1]
        First = self.counts[letter]; Last = self.counts[NEXT_LETTER[letter]] - 1;
        
        for i in reversed(range(len(pattern)-1)):
            letter = pattern[i]
            First = self.counts[letter] + self.occs[letter][First-1]
            Last = self.counts[letter] + self.occs[letter][Last] - 1
            if Last < First:
                return None
        
        return First, Last + 1

    def occurrence_number(self, pattern):
        
        First, Last = self.backward_search(pattern)
        return Last - First
    
    def occurrence_positions(self, pattern):
        
        First, Last = self.backward_search(pattern)
        return sorted([self.mark[i] for i in range(First, Last)])

def pattern_search(text, pattern):
    
    size_text = len(text)
    size_pattern = len(pattern)
    pos = list()
    for index in range(size_text - size_pattern):
        if text[index:index+size_pattern] == pattern:
            pos.append(index)
    return pos
