
b = [22, 25, 28, 28, 33, 36, 37, 41, 41, 41, 47, 48, 52, 55, 55, 60, 60]


def new_list(a):
    new_list = []
    for i in a:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

new_list(b)
