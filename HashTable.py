# HASH TABLE
# Each element contains key-value pairs
# Keys are unique integers used for indexing values
# Values are the data associated with the keys
# Applications
#   - cryptography
#   - constant time lookup and insertion
#   - indexing of data
# TODO: Implement Linear Probing Collision Handling

# CHAINING COLLISION HANDLING

# Create HashTable
# Array of 5 arrays
HT = [[] for _ in range(5)]

# Hash Function
# Used to determine index for where to store element linked with the key
def hash(key):
    # k % m, where k is the key value and m is the length of the Hashtable
    return key % len(HT)

# Insert Function
# HashTable: where we insert the value
# Keyvalue: determine index for where to place the value in the Hashtable
# Value: value to be inserted in the Hashtable
def insert(Hashtable, keyvalue, value):

    # Get the Hash Key
    hash_key = hash(keyvalue)

    # Append the value at the hash_key of the hashtable
    Hashtable[hash_key].append(value)


# TEST

# Insert 
# Since we're just chaining, if they're the same index, the values will just get added to the same array
# 0 modulo
insert(HT, 10, "1")
insert(HT, 20, "2")
insert(HT, 30, "3")
insert(HT, 40, "4")
insert(HT, 50, "5")

# 1 modulo
insert(HT, 11, "1")
insert(HT, 21, "2")
insert(HT, 31, "3")
insert(HT, 41, "4")
insert(HT, 51, "5")

# 3 modulo
insert(HT, 13, "1")
insert(HT, 23, "2")
insert(HT, 33, "3")
insert(HT, 43, "4")
insert(HT, 53, "5")

print(HT)
