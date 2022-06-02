def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'Raymund')
insert(HashTable, 25, 'May')
insert(HashTable, 20, 'Stephanie')
insert(HashTable, 9, 'Gregorio')
insert(HashTable, 21, 'Abdol')
insert(HashTable, 21, 'Hannah')

display_hash(HashTable)
