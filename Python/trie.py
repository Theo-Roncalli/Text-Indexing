#!/usr/bin/env python3

from ete3 import Tree

def trie_insert(trie, word, index):
    """
    Insert word in a trie and add its index.
    
    Input:
        trie: a trie (ete3.Tree)
        word: a string
        index: an integer corresponding to the word index
    
    Result:
        Modifies input trie. It inserts new branches in alphabetical order
    """
    
    if not word:
        if hasattr(trie, "index"):
            trie.index.append(index)
        else:
            trie.add_features(index = [index])
    else:
        pos = -1
        for i, child in enumerate(trie.children):
            if child.name >= word[0]:
                pos = i
                break
        
        if pos == -1:
            trie.children.append(Tree(name = word[0]))
        elif trie.children[pos].name != word[0]:
            trie.children.insert(pos, Tree(name = word[0]))
        
        trie_insert(trie.children[pos], word[1:], index)

def trie_construct(words):
    """
    Construct a trie from a list of words
    
    Input:
        words: a list of strings
    
    Output:
        trie containing the words, annotated with the words indices
    """

    trie = Tree()
    
    for index, word in enumerate(words):
        trie_insert(trie, word, index)

    return trie

def trie_print(trie):
    """
    Print trie
    
    Input:
        trie: a trie (ete3.Tree) with annotation
    
    Result:
        Print a trie to the stdout.
    """
    print(trie.get_ascii(show_internal = True, attributes=["name", "index"]))

