#horner's method
def hornerHash(key, base, mod): 
    hashValue = 0 # intializes value to 0
    for char in key: # iterates through every character in the key
        # updates the value usung horner's method
        hashValue = (hashValue * base + ord(char)) % mod
    return hashValue # returns the value
key = "hello"
base = 16
mod = 10000000
index = hornerHash(key, base, mod)
print("Hash index:", index)