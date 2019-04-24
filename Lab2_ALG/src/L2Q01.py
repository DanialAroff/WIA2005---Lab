class HashTable:
    def __init__(self):
        self.size = 5
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def printall(self):
        position = 0
        while True:
            if self.slots is not None:
                print(self.slots[position], '|', self.data[position])
            position = position + 1
            if position == len(self.slots):
                break

    def hash(self, astring, tablesize):
        summ = 0
        for i in range(len(astring)):
            summ = summ + ord(astring[i])

        return summ % tablesize

    def hashfunction(self, key, size):
        key = self.hash(key, size)
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        # increase hash table size
        if self.halffull():
            self.size = self.size*2
            for n in range(len(self.slots), len(self.slots)*2):
                self.slots.append(None)
                self.data.append(None)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))  # linear probing
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))  # linear probing
                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace if there's already a data
        print(hashvalue, 'for', data)  # testing purpose

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))  # move to next hash
                if position == startslot:  # if the position returned to the start slot then the key does not exist.STOP
                    stop = True
        return data

    #  additional function to check if hash table is half full
    def halffull(self):
        c = False
        counter = 0
        for i in range(len(self.slots)):
            if self.data[i] is not None:
                counter = counter + 1
        if counter >= len(self.slots)/2:
            c = True
        return c

    def delete(self, key):
        for n in range(len(self.slots)):
            if self.slots[n] == key:
                self.slots[n] = None
                self.data[n] = None


H = HashTable()

while True:
    try:
        selection = int(input('\n(1)Add (2)Delete (3)Display (4)Quit  : '))

        if selection == 1:
            reg = input('\nRegistration number: ')
            name = input('Name: ')
            H.put(reg, name)
            print(name, 'registered')
            H.printall()
        elif selection == 2:
            reg = input('\nRegistration number: ')
            H.delete(reg)
            print(reg, 'deleted')
            H.printall()
        elif selection == 3:
            H.printall()
        else:
            break
    except ValueError:
        print('Input was not a integer! - please try again')
