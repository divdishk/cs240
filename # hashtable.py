# hashtable using seprate chaining 
class hashTable:
    def __init__(self, size, hashFunction): 
        """
        intializes the hash table
        size = size of hash table
        hashFunction: the function used to compute the hash index
        """
        self.size = size
        self.hashFunction = hashFunction
        self.table = [[] for _ in range(size)]
    
    def insert(self, key, value): # inserts a key-value pair into the hash table
        # key: key of the key-value pair
        # value: value of the key-value pair
        index = self.hashFunction(key) % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                # updates the value if the key already exists
                pair[1] = value
                return
        # appends a new key-value pair to the appropriate bucket
        self.table[index].append([key, value])

    def get(self, key): # retrives the value associated with a given key from the hash table
        index = self.hashFunction(key) % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1] # return value associated with they key
        return None # return None if key not found
    
    def remove(self, key): # removes a key-value pair from the hash table
        index = self.hashFunction(key) % self.size
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
            
def hornerHash(key, base, mod): #computes the hash value for a given key using Horner's method
        hashValue = 0
        for char in key:
            hashValue = (hashValue * base + ord(char)) % mod
        return hashValue # computed hash value
    
hash_table = hashTable(10, hornerHash)
hash_table.insert("hello", 5)
hash_table.insert("world", 10)

print(hash_table.get("hello"))
print(hash_table.get("world"))

hash_table.insert("hello", 15)
print(hash_table.get("hello"))

hash_table.remove("hello")
print(hash_table.get("hello"))

