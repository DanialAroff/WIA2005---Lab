import hashtable
import collections


def getfrequency(mylist, myword):
    counter = collections.Counter(mylist)
    freq = 0  # to hold the value of frequencies
    keys = list(counter.keys())
    values = list(counter.values())
    for w in range(len(keys)):
        if keys[w] == myword:
            freq = values[w]
            break
    return freq


h = hashtable.HashTable()
f = open('input.txt', 'r')
# create a list of every words of the txt file
mylist = f.read().split()
for i in range(len(mylist)):
    # all words are changed to lowercase and full stop is removed
    mylist[i] = mylist[i].lower().replace(".", "")

for n in range(len(mylist)):
    word = mylist[n]
    frequency = getfrequency(mylist, word)
    h.put(word, frequency)
h.printall()
