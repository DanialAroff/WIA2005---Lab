import collections
from hashtable import HashTable
from BinarySearchTree import BST

tree = BST()

tree.insert(20)
tree.insert(3)
tree.insert(12)
tree.insert(5)
tree.insert(9)
tree.insert(10)
tree.inorder()
print('Deleting node 5\n')
tree.delete(1)
print('Root is ' + str(tree.get_root().data))
tree.inorder()
# print('Minimum value in the Tree: ' + str(tree.min_value_node()))






# doo =input('Enter a string: ')
# sum = 0
# for i in range(0, len(doo), 1):
#     sum = sum + ord(doo[i])
#     print(ord(doo[i]), end=" ")
#
# print('\n\n' + str(sum))
# print('hash:', str(sum % 5))

# l = ['pikachu', 'eevee', 'aron', 'bulbasaur', 'eevee', 'squirtle', 'pikachu', 'rowlet', 'rowlet', 'rowlet', 'aron']
# myword = input('Pokemon   ')
#
# counter = collections.Counter(l)
# keys = list(counter.keys())
# values = list(counter.values())
# for n in range(len(keys)):
#     if keys[n] == myword:
#         print(keys[n], values[n])
#         break
h = HashTable()

