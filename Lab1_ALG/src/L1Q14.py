
def reverse_string(s: str):
    word_list = s.split()
    for i in range(len(word_list)-1, -1, -1):
        print(word_list[i], end=" ")


user_string = input('Enter a string: ')
reverse_string(user_string)
