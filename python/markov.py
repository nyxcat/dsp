#!/usr/bin/env python          A                                                                                   

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
import csv
import re

filename = sys.argv[1]
wordnum = int(sys.argv[2])

frequency = {}
totalnum = {}
beginfrequency = {}
beginnum = 0

with open(filename) as txtfile:
    text = txtfile.read()
    sentences = text.split('\n\n')
    for sentence in sentences:
        wordinsentence = sentence.split()
        if len(wordinsentence) == 0:
            continue
        beginnum += 1
        beginword = wordinsentence[0]
        if beginword in beginfrequency:
            beginfrequency[beginword] += 1
        else:
            beginfrequency[beginword] = 1
    words = re.split('\n| ',text)
    for i, word in enumerate(words):
        if word == '':
            words.pop(i)
    for i, word in enumerate(words[:-2]):
        if word in frequency:
            totalnum[word] += 1
            if words[i+1] in frequency[word]:
                frequency[word][words[i+1]] += 1
            else:
                frequency[word][words[i+1]] = 1
        else:
            frequency[word] = {words[i+1]: 1}
            totalnum[word] = 1
txtfile.close()

for word, value in beginfrequency.items():
    beginfrequency[word] = value/beginnum
for word, totalnum in totalnum.items():
    if totalnum != 0:
        for nextword, num in frequency[word].items():
            frequency[word][nextword] = num/totalnum

preword = np.random.choice(list(beginfrequency.keys()),
                           p = list(beginfrequency.values()))
pseudotext = '' + preword

for i in range(wordnum - 1):
    pseudotext += ' '
    preword = np.random.choice(list(frequency[preword].keys()),
                                p = list(frequency[preword].values()))
    pseudotext += preword
print(pseudotext)
 

