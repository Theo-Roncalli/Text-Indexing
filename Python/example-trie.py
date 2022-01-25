#!/usr/bin/env python3

import Trie

print("\n--------------Prefix Tree--------------\n")

text = "bannamabananpananasbanana"
words = ["ananas", "anna", "ann", "banana", "banama", "anaba"]
trie = Trie.Trie(words = words)

print(trie, "\n\n")

occurrences = trie.pattern_search(text)
for (i,k) in occurrences:
    print("{:2}: {}".format(i, words[k]))

print("\n--------------Suffix Tree--------------\n")

text = "ananasbanana$"
suffix_tree = Trie.SuffixTree(text, compression = False)
print(suffix_tree)

suffix_tree.compress()
print(suffix_tree)

pattern = "ana"
occurrences = suffix_tree.pattern_search(pattern)
print("\nWe can find the pattern \"", pattern, "\" in the sequence \"", text, "\" at positions ", occurrences, sep = "")

