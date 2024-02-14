# hashtable using probing
class HashTable:
    def __init__(self, size): # intializes a hash table with a given size
        self.size = size
        self.table = [None] * size

    def hashFunction(self, key): # computes a hash value for a given key
        return hash(key) % self.size

    def insert(self, key, value): # inserts  akey-value pair into hash table
        index = self.hashFunction(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            # Linear probing to find the next available slot
            nextIndex = (index + 1) % self.size
            while nextIndex != index:
                if self.table[nextIndex] is None:
                    self.table[nextIndex] = (key, value)
                    return
                nextIndex = (nextIndex + 1) % self.size
            raise ValueError("Hash table is full")

    def get(self, key): # retrieves the value associated with a given key
        index = self.hashFunction(key)
        startIndex = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1] # returns the associated value with they key
            index = (index + 1) % self.size
            if index == startIndex:  # Reached the starting point, key not found
                break
        return None # returns none if key not found

    def remove(self, key): # removes a key-value pair from the hash table
        index = self.hashFunction(key)
        startIndex = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == startIndex:  # Reached the starting point, key not found
                break
        raise KeyError("Key not found in hash table")

# Example usage:
hashTable = HashTable(10)
hashTable.insert("hello", 5)
hashTable.insert("world", 10)

print(hashTable.get("hello"))  # Output: 5
print(hashTable.get("world"))  # Output: 10

hashTable.insert("hello", 15)
print(hashTable.get("hello"))  # Output: 15

hashTable.remove("hello")
print(hashTable.get("hello"))  # Output: None
