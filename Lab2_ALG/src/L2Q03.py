# Runway Reservation System


def sortArray(A):
    for i in range(0, len(A)):
        for j in range(1, len(A)-1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
    return A


R = [None]  # set of landing request
i = 0
print('Runway Reservation System\n')
while True:
    n_request = int(input('Enter number of request: '))
    R = [None]*n_request
    print()
    for i in range(0, n_request):
        R[i] = input('Landing time for request ' + str(i+1) + ': ')
    R = sortArray(R)
    print(R)


rt = Node(20)
rt.insert(rt, Node(3))
rt.insert(rt, Node(12))
rt.insert(rt, Node(5))
rt.insert(rt, Node(9))
rt.insert(rt, Node(10))

print('In-order traversal')
rt.inorder(rt)
rt.deleteNode(rt, 10)
print('\n')
rt.inorder(rt)

