#!/usr/bin/env python                                                                                             

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:                                   

# ```bash                                                                                                         
# ./markov.py chains.txt 40                                                                                       
# ```                                                                                                             

# A possible output would be:                                                                                     

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.                                                                                               

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.                                                                                             

import numpy as np
import sys
import random

filename = sys.argv[1]
wordnum = int(sys.argv[2])

frequency = {}
totalnum = {}

with open(filename) as txtfile:
    s = txtfile.read()
    i = 0
    while i < (len(s)-2):
        print(i)
        while s[i] == '\\' or s[i] == '\n':
            i += 1
            if i+2 >= len(s):
                break
        index_first = ord(s[i]) - ord(' ')
        if (index_first < 0) or (index_first > 95):
            i += 1
            continue
        while s[i+1] == '\\' or s[i+1] == '\n':
            i += 1
            if i+2 >= len(s):
                break
        index_second = ord(s[i+1]) - ord(' ')
        if index_second < 0 or index_second > 95:
            i += 1
            continue
        while s[i+2] == '\\' or s[i+1] == '\n':
            i += 1
            if i+2 >= len(s):
                break
        index_third = ord(s[i+2]) - ord(' ')
        if index_third < 0 or index_third > 95:
            i += 1
            continue
        if (s[index_first] + s[index_second]) in frequency:
            frequency[s[index_first]+s[index_second]][index_third] += 1
            totalnum[s[index_first]+s[index_second]] += 1
        else:
            frequency[s[index_first]+s[index_second]] = np.zeros(95)
            frequency[s[index_first]+s[index_second]][index_third] = 1
            totalnum[s[index_first]+s[index_second]] = 1
        i += 1
txtfile.close()

for key, value in totalnum.items():
    frequency[key] = frequency[key] / value
print(totalnum['. '])
'''count = 0
string = ''
string += chr(random.choices(range(0,95), frequency['  '])[0] + ord(' '))
string += chr(random.choices(range(0,95), frequency[' '+string[0]])[0] + ord(' '))
while count < wordnum:
    c_firsttwo = string[-2:]
    c = chr(random.choices(range(0,95), frequency[c_firsttwo])[0] + ord(' '))
    string += c
    if c == ' ':
        count += 1
print(string)
'''
