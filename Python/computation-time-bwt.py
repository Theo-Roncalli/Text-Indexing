#!/usr/bin/env python3

import SuffixArray as sa
import BurrowsWheeler as bw

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
bwt = bw.BurrowsWheeler(text)
end = time.time()
print("time to build bwt:", end-start)
del start, end, bwt

start = time.time()
suffix_array = sa.SuffixArray(text);
end_sa = time.time()
bwt = bw.BurrowsWheeler(text, suffix_array);
end_bwt = time.time()
print("time to build sa:", end_sa-start)
print("time to build sa and then bwt:", end_bwt-start)
print("time to build bwt from sa:", end_bwt-end_sa)
