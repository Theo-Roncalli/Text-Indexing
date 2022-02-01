#!/usr/bin/env python3

import Trie

print("\n------------------------Prefix Tree------------------------\n")

text = "bannamabananpananasbanana"
words = ["anna", "ananas", "banane", "bananes", "antilles", "ananas"]
trie = Trie.Trie(words = words)

print(trie, "\n\n")

occurrences = trie.pattern_search(text)
for (i,k) in occurrences:
    print("{:2}: {}".format(i, words[k]))

print("\n------------------------Suffix Tree------------------------\n")

text = "ananas"
suffix_tree = Trie.SuffixTree(text, compression = False)
print(suffix_tree)

pattern = "anab"
occurrences = suffix_tree.pattern_search(pattern)
print("\nWe can find the pattern \"", pattern, "\" in the sequence \"", text, "\" at positions ", occurrences, sep = "")

