# hash table with collision resolution by linear probing
size = int(input("Enter the size of the hash table: "))
hash_table = [None] * size
def hash_function(key):
    return int(key) % size
def insert():
    key = input("Enter the key to be inserted: ")
    index = hash_function(key)
    if hash_table[index] == None:
        hash_table[index] = key
    else:
        while hash_table[index] != None:
            index = index + 1
            if index == size:
                index = 0
        hash_table[index] = key
def delete():
    key = input("Enter the key to be deleted: ")
    index = hash_function(key)
    if hash_table[index] == key:
        hash_table[index] = None
    else:
        while hash_table[index] != key:
            index = index + 1
            if index == size:
                index = 0
        hash_table[index] = None
def search():
    key = input("Enter the key to be searched: ")
    index = hash_function(key)
    if hash_table[index] == None:
        print("Key not found")
    else:
        while hash_table[index] != key:
            index = index + 1
            if index == size:
                index = 0
        print("Key found at index: ", index)
def display():
    for i in range(size):
        print(hash_table[i], end = " ")
    print()
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        search()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

