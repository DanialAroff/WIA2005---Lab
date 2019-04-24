word = input("Pick a word or name: ")
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
if word.lower() == reversed_word.lower():
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")
print("\n" + reversed_word.lower())
