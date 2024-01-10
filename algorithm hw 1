
# function to read value from a file into an array
def read_file_to_array(fileName):
   with open(fileName, "r") as file: # opens the file in read mode and automatically closes
      # reads each line of file
      array = [line.strip() for line in file]
   return array

# function to implent a binary search algorithm
def binary_search(array, target):
   counter = 0 
   left = 0
   right = len(array) - 1
   
   # loop to binary search
   while left <= right:
      counter += 1 # counts how many iterations it took to get target value
      mid = (left + right) // 2 # middle element 
      current = int(array[mid])
      # checks if current value equals to the targeted value 
      if current == target:
         return mid, counter
      elif current > target: # checks if the value is too high than target
         right = mid - 1
      else: # checks if value is too low
         left = mid + 1
   # returns -1 if the target is not found, as well as the # of iterations
   return -1, counter 


target = 51216352
fileName = 'numbers.txt'

# reads the values from the file into an array
array = read_file_to_array(fileName)

# performs binary search
result, counter = binary_search(array, target)

# outputs the results and # of iterations 
if result != -1:
    print(f"Target {target} found at index {result} with {counter} iterations.")
else:
    print(f"Target {target} not found after {counter} iterations.")
   
