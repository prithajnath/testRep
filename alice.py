#!bin/usr/python

import nltk
import matplotlib.pyplot as plt
import math

alice_words = nltk.corpus.gutenberg.words('carroll-alice.txt')
alice_freq = nltk.FreqDist(alice_words)
alice_log = [x for x in map(math.log,alice_freq.values())]

alice_sorted_freq = alice_freq.most_common()
        
#print(alice_sorted_freq)

alice_word_index = {}

for i in range(len(alice_words)):
    alice_word_index[alice_words[i]] = i

#print(alice_word_index)

#x = [math.log(alice_word_index[m[0]]) for m in alice_sorted_freq]
#y = [math.log(n) for n in list(alice_freq.values())]
#y.sort(reverse=True)


y = [math.log(m[1]) for m in alice_sorted_freq]

x = [math.log(n) for n in range(1,len(alice_sorted_freq)+1)]

#print(x)

#alist = list(alice_freq.values())
#alist.sort(reverse=True)
#print(y)

plt.plot(x,y)
plt.legend()
plt.show()



