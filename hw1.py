
def read_file_to_array(fileName):
   with open('numbers.txt', "r") as file: # automatically closes file
      array = [line.strip() for line in file]
   return array

def binary_search(array, target):
   counter = 0
   left = 0
   right = len(array) - 1
   
   while left <= right:
      counter += 1
      mid = (left + right) // 2
      current = array[mid]
      if current == target:
         return mid
      elif guess > item:
         right = mid - 1
      else:
         left = mid + 1

   target_value = 51216352
   fileName = "number.txt"
   array = read_file_to_array(fileName)
   result, counter = binary_search(array, target_value)
   print(result, counter)
   
   return None, counter
   