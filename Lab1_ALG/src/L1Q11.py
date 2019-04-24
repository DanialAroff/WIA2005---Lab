a = [5, 10, 15, 20, 25]


def my_list(L):
    another_list = [L[0], L[-1]]
    return another_list


print('Initial list', a)
print('New list', my_list(a))
