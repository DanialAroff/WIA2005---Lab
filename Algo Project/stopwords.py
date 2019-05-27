import collections

file = open('list of stopwords.txt', 'r')

# create a list
list_of_stopwords = file.read().split()
file.close()
print(list_of_stopwords)
