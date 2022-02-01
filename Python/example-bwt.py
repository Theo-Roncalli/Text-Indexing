#!/usr/bin/env python3

import BurrowsWheeler as bw
import time

print("\n------------------------Burrows Wheeler Transformation------------------------\n")

pattern = "ana"
text = None
path = "romeo_juliette_long.txt"

if text and path:
    raise TypeError("We must choose between either text or path argument.")
elif not text and path:
            with open(path, 'r') as file:
                text = file.read()

print("The size of the text is ", len(text), sep = "")

bwt = bw.BurrowsWheeler(text)
print("The size of the bwt is ", len(bwt.bwt), sep = "")

bwt.compress()
# print("Burrows Wheeler transform after encoding = ", bwt, sep = "")
print("The size of the compressed bwt is ", len(bwt.bwt), sep = "")

bwt.decompress()
# print("Burrows Wheeler transform after decoding = ", bwt, sep = "")
print("The size of the decompressed bwt is ", len(bwt.bwt), sep = "")

start = time.time()
res = bw.pattern_search(text, pattern)
# res = text.count(pattern)
end = time.time()
print("The occurrences with full scan: ", res, " and the computational time is: ", end-start, sep="")
del start, end, res

start = time.time()
res = bwt.pattern_search(pattern)
end = time.time()
print("The occurrences with bwt indexing: ", res, " and the computational time is: ", end-start, sep="")
