#!/usr/bin/env python3

import SuffixArray

print("\n------------------------Suffix Array------------------------\n")

text = "ananasbanana $"
pattern = "ana"

suffix_array = SuffixArray.SuffixArray(text)
print("Suffix Array = ", suffix_array, sep = "")

occurrences = suffix_array.pattern_search(text, pattern)
print("We can find the pattern \"", pattern, "\" at positions ", occurrences, sep = "")
