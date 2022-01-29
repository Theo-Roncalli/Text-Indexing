#!/usr/bin/env python3

import SuffixArray
import Trie
import time

print("\n------------------------Computation time------------------------")

text = """PROLOGUE

    Two households, both alike in dignity,
    In fair Verona, where we lay our scene,
    From ancient grudge break to new mutiny,
    Where civil blood makes civil hands unclean.
    From forth the fatal loins of these two foes
    A pair of star-cross'd lovers take their life;
    Whose misadventured piteous overthrows
    Do with their death bury their parents' strife.
    The fearful passage of their death-mark'd love,
    And the continuance of their parents' rage,
    Which, but their children's end, nought could remove,
    Is now the two hours' traffic of our stage;
    The which if you with patient ears attend,
    What here shall miss, our toil shall strive to mend.$"""

start = time.time()
suffix_array = SuffixArray.SuffixArray(text)
end = time.time();
print("time to build sa from ordered suffix pairs:", end-start)
del start, end, suffix_array

start_from_nothing = time.time()
suffix_tree = Trie.SuffixTree(text, compression = False); start_from_trie = time.time();
suffix_array = SuffixArray.SuffixArray(trie = suffix_tree)
end = time.time();
print("time to build trie and then sa:", end-start_from_nothing)
print("time to build sa from trie:", end-start_from_trie)

