# Text-Indexing

This work focuses on the first indexing algorithm proposed in [Ferragina and Manzini (2005)](https://www.researchgate.net/publication/220430619_Indexing_compressed_text). The indexing proposed is based on the Burrows-Wheeler Transformation (BWT). In our implementation, some simplifications have been made in order to make the code easier to write. As a consequence, the algorithm takes lot of RAM memory. For instance, we have store all mappings between the indices of the BWT string and a text with an full array. Also, there is a function or data structure that can be improved: $\occs\left(c, i\right)$ who corresponds to the number of occurrences of a character $c$ in the prefix of the Burrows-Wheeler Transformation $BWT_{1:i}$. Hence, the realised implementation is not competitive in terms of spatial complexity but it gives a preliminary code for indexing. Note also that the implementation does not use the indexing on the compressed BWT, but only on the BWT.

## Use modules

Three modules are porposed: (1) _Trie_, (2) _SuffixArray_, and (3) _BurrowsWheeler_. This is this last module that is based on the work of [Ferragina and Manzini (2005)](https://www.researchgate.net/publication/220430619_Indexing_compressed_text). For using these modules, please type:
```bash
git clone https://github.com/Theo-Roncalli/Text-Indexing.git
cd Text-Indexing/Python
```
and launch your IDE for using _Python_.
