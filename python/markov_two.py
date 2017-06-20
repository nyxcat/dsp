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

def beginwordfrequency(filename):
    beginfrequency = {}
    beginnum = 0
    with open(filename) as txtfile:
        text = txtfile.read()
        sentences = text.split('\n\n')
        for sentence in sentences:
            wordinsentence = sentence.split()
            if len(wordinsentence) < 2:
                continue
            beginnum += 1
            beginword = wordinsentence[0]
            if beginword in beginfrequency:
                beginfrequency[beginword] += 1
            else:
                beginfrequency[beginword] = 1
    txtfile.close()
    for word, value in beginfrequency.items():
        beginfrequency[word] = value/beginnum
    return beginfrequency

def secondwordfrequency(filename):
    secondfrequency = {}
    secondtotalnum = {}
    with open(filename) as txtfile:
        text = txtfile.read()
        sentences = text.split('\n\n')
        for sentence in sentences:
            wordinsentence = sentence.split()
            if len(wordinsentence) < 2:
                continue
            beginword = wordinsentence[0]
            secondword = wordinsentence[1]
            if beginword in secondfrequency:
                secondtotalnum[beginword] += 1
                if secondword in secondfrequency[beginword]:
                    secondfrequency[beginword][secondword] += 1
                else:
                    secondfrequency[beginword][secondword] = 1
            else:
                secondtotalnum[beginword] = 1
                secondfrequency[beginword] = {secondword: 1}
        text = txtfile.read()
    txtfile.close()
    for word, totalnum in secondtotalnum.items():
        for nextword, num in secondfrequency[word].items():
            secondfrequency[word][nextword] = num/totalnum
    return secondfrequency

def thirdwordfrequency(filename):
    thirdfrequency = {}
    thirdtotalnum = {}
    with open(filename) as txtfile:
        text = txtfile.read()
        words = re.split('\n| ',text)
        for i, word in enumerate(words):
            if word == '':
                words.pop(i)
        for i, word in enumerate(words[:-3]):
            firsttwowords = words[i] + words[i+1]
            if firsttwowords in thirdfrequency:
                thirdtotalnum[firsttwowords] += 1
                if words[i+2] in thirdfrequency[firsttwowords]:
                    thirdfrequency[firsttwowords][words[i+2]] += 1
                else:
                    thirdfrequency[firsttwowords][words[i+2]] = 1
            else:
                thirdfrequency[firsttwowords] = {words[i+2]: 1}
                thirdtotalnum[firsttwowords] = 1
    txtfile.close()
    for word, totalnum in thirdtotalnum.items():
        for nextword, num in thirdfrequency[word].items():
            thirdfrequency[word][nextword] = num/totalnum
    return thirdfrequency    


def main(filename, wordnum):
    pseudotext = ''

    if wordnum == 0:
        return pseudotext
    bwfre = beginwordfrequency(filename)
    
    firstword = np.random.choice(list(bwfre.keys()), p = list(bwfre.values()))
    pseudotext += firstword

    if wordnum == 1:
        return pseudotext

    swfre = secondwordfrequency(filename)
    
    secondword = np.random.choice(
        list(swfre[firstword].keys()), p = list(swfre[firstword].values()))

    pseudotext = pseudotext + ' ' + secondword

    if wordnum == 2:
        return pseudotext

    twfre = thirdwordfrequency(filename)

    for i in range(wordnum - 2):
        pseudotext += ' '
        thirdword = np.random.choice(
            list(twfre[firstword+secondword].keys()),
            p = list(twfre[firstword+secondword].values()))
        pseudotext += thirdword
        firstword = secondword
        secondword = thirdword
    print(pseudotext)

main(filename, wordnum)
