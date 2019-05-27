
positive = open('wordlist/list of positive words.txt', 'r')
negative = open(r'wordlist/list of negative words.txt', 'r')

p = positive.read().split(',')
for i in range(len(p)):
    if p[i][0] == ' ':
        p[i] = p[i][1:]
positive2 = open('wordlist/positivewords.txt', 'w', encoding='utf-8')
[positive2.write(word + '\n') for word in p]

n = negative.read().split(',')
for i in range(len(n)):
    if n[i][0] == ' ':
        n[i] = n[i][1:]
negative2 = open('wordlist/negativewords.txt', 'w', encoding='utf-8')
[negative2.write(word + '\n') for word in n]

print(p)

positive.close()
positive2.close()
negative.close()
negative2.close()
