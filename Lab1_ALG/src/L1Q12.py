def generatefibonacci(f):
    fibonacci = [0, 1]
    previous_1 = 1
    
    previous_2 = 0  # 0, 1, ?, ?
    if f > 2:
        for i in range(2, f, 1):
            current = previous_2 + previous_1
            fibonacci.append(current)
            previous_2 = previous_1
            previous_1 = current
    return fibonacci


print('The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of '
      'previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8 ,13,....\n')
frequency = int(input('How many Fibonacci numbers you want to generate? '))
print(generatefibonacci(frequency))
