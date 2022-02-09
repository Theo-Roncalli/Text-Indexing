#!/usr/bin/env python3

import sys
import BurrowsWheeler as bw
import time

def help():
    print("""Use: python time-bwt.py <path> <pattern>
Launch a pattern search on a text.

options:
    -h, --help                  Documentation on the script
    """)

if "-h" in sys.argv or "--help" in sys.argv:
    help()
    sys.exit()

try:
    path = sys.argv[1]
    pattern = sys.argv[2]
except:
    help()
    print('ERROR : please enter a path and a pattern.')
    sys.exit()

with open(path, 'r') as file:
    text = file.read()

start1 = time.time()
bwt = bw.BurrowsWheeler(text)
end1 = time.time()
time1 = end1 - start1
print("\n------------------------Burrows Wheeler Transformation------------------------\n")
print("Time for building the bwt: ", time1, " sec.", sep = "")

start2 = time.time()
bwt.compress()
end2 = time.time()
time2 = end2 - start2

print("\n------------------------Compression------------------------\n")
print("Time (run-length encoding): ", time2, " sec.", sep = "")
print("Length (text): ", len(text), "char.", sep = "")
print("Length (compressed bwt): ", len(bwt), " char.", sep = "")

bwt.decompress()

start3 = time.time()
res = bw.pattern_search(text, pattern)
end3 = time.time()
time3 = end3 - start3
print("\n------------------------Pattern search with full scan------------------------\n")
print("Positions:", res, sep="")
print("Time: ", time3, " sec.", sep="")

start4 = time.time()
res = sorted(bwt.occurrence_positions(pattern))
end4 = time.time()
time4 = end4 - start4
print("\n------------------------Pattern search with BWT------------------------\n")
print("Positions:", res, sep="")
print("Time: ", time4, " sec.", sep="")

print("\n------------------------Difference------------------------\n")
print("BWT indexing is ", time3/time4, " times faster than full scan", sep="")
