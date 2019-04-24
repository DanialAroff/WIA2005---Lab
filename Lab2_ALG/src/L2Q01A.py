studdict = {}

while True:
    reg = input('\nRegistration number: ')
    name = input('Student\'s name: ')
    studdict[reg] = name
    print('inputting ' + name + ' with key ' + reg)
    check = int(input('\nContinue? (enter 0 to exit)\n'))
    if check is 0:
        print()
        break
    
for x in studdict:
    print(x + '|' + studdict[x])
    
while True:
    act = int(input('\n(1)Add (2)Delete (3)Print (4)Exit   :'))
    if act is 1:
        reg = input('\nRegistration number: ')
        name = input('Student\'s name: ')
        studdict[reg] = name
        print('inputting ' + name + ' with key ' + reg)
    elif act is 2:
        reg = input('Registration number: ')
        studdict.pop(reg)
        print(reg + ' removed')
    elif act is 3:
        for x in studdict:
            print(x + '|' + studdict[x])
    elif act is 4:
        break
