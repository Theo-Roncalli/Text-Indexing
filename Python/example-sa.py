#!/usr/bin/env python3

import SuffixArray as sa

print("\n------------------------Suffix Array------------------------\n")

text = "ananasbanana$"
pattern = "ana"
path = None

if text and path:
    raise TypeError("SuffixArray __init__() takes either text or path argument")
elif not text and path:
            with open(path, 'r') as file:
                text = file.read()
            if text[-1] != "$": text += "$"

suffix_array = sa.SuffixArray(text)
print("Suffix Array = ", suffix_array, sep = "")
occurrences = suffix_array.pattern_search(text, pattern)
print("We can find the pattern \"", pattern, "\" at position(s) ", occurrences, sep = "")
print("Indeed, at position ", occurrences[0], " for instance, we have: ", text[occurrences[0]:occurrences[0]+len(pattern)], sep = "")