# Binary search recursively
def read_file_to_array(fileName):
   with open(fileName, "r") as file: # opens the file in read mode and automatically closes
      # reads each line of file
      array = [line.strip() for line in file]
   return array

# recursive function to implent a binary search algorithm
def binarySearchRecursive(array, target, left, right, counter = 0):
   
   # loop to binary search
   while left <= right:
      counter += 1 # counts how many iterations it took to get target value
      mid = (left + right) // 2 # middle element 
      current = int(array[mid])
      # checks if current value equals to the targeted value 
      if current == target:
         return mid, counter
      elif current > target: # checks if the value is too high than target
         return binarySearchRecursive(array, target, left, mid-1, counter)
      else: # checks if value is too low
         return binarySearchRecursive(array, target, mid+1, right, counter)
   # returns -1 if the target is not found, as well as the # of iterations
   return -1, counter 

# Reads the file and sorts the array
fileName = 'numbers-3.txt'
array = read_file_to_array(fileName)
array.sort()

target = 5842193

# performs binary search recursively 
result, counter =  binarySearchRecursive(array, target, 0, len(array)-1)

# outputs the results and # of iterations 
if result != -1:
    print(f"Target {target} found at index {result} with {counter} iterations.")
else:
    print(f"Target {target} not found after {counter} iterations.")
   