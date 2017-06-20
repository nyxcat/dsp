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

frequency = [(np.zeros(95)) for x in range(95)]
n = np.zeros(95)

with open(filename) as txtfile:
    s = txtfile.read()
    for i in range(len(s)-1):
        index_bef = ord(s[i]) - ord(' ')
        if s[i] != '\\' and s[i+1] != '\\':
            index_aft = ord(s[i+1]) - ord(' ')
        elif (s[i+1] == '\\') and (i < len(s) - 2):
            index_aft = ord(s[i+2]) - ord(' ')
            i += 1
        else:
            break
        if index_aft >= 0 and index_aft < 95 and index_bef >= 0 and index_bef < 95 and index_aft+index_bef > 0:
            frequency[index_bef][index_aft] += 1
            n[index_bef] += 1
txtfile.close()

for i in range(len(n)):
    if n[i] != 0:
        for j in range(95):
            frequency[i][j] = frequency[i][j] / n[i]

count = 0
string = ''
string += chr(random.choices(range(0,95), frequency[0])[0])
while count < wordnum:
    c_bef = string[-1]
    c_bef_index = ord(string[-1]) - ord(' ')
    c = chr(random.choices(range(0,95), frequency[c_bef_index])[0] + ord(' '))
    string += c
    if c == ' ':
        count += 1
print(string)
