#!/usr/bin/env pypy
'''
Created on Jan 22, 2017

@author: Hector
'''

import re
import sys

#######################   PART B  ######################################################
def make_set(Filepath):
    tokens = set()
    prog = re.compile('[^0-9a-zA-Z]+')
    with open(Filepath) as infile:
        for line in infile:
            line = prog.sub(' ',line).split()
            for  word in line:
                tokens.add(word.lower())
    return tokens
    
def compareTokens(infile1, infile2):
    tokens1 = make_set(infile1)
    tokens2 = make_set(infile2)
    shared_tokens = tokens1 & tokens2
    print len(shared_tokens)
    
def ptokens(s):
    print(len(s))
    #S
    
if __name__ == '__main__':
    infile1 = sys.argv[1]
    infile2 = sys.argv[2]
    compareTokens(infile1,infile2)