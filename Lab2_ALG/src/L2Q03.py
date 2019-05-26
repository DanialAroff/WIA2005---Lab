# Runway Reservation System
import time
from BinarySearchTree import BST

R = [None]  # set of landing request
t = 0
tree = BST()

print('Runway Reservation System\n')
while True:
    tw = int(input('Input landing time request: '))
    if tw < 0:
        break
    else:
        if R[0] is not None:
            R.append(tw)
        else:
            R[0] = tw
print(R)

# while True:
#     if tree.search(t):
#         print('Reference time t(now): ' + str(t))
#     t = t + 1
#     time.sleep(0.5)
