# Insertion Sort

def readFile(fileName):
   with open(fileName, "r") as file: # opens the file in read mode and automatically closes
      # reads each line of file
      array = [int(line.strip()) for line in file]
   return array

def insertion_sort(array):
        # iterates through each element in the array starting from the second element
    for i in range(1, len(array)):
       # stores the current element to be instered in the sorted part
       key = array[i]

        # moves elements greater than key to one position bigger than current positon
       j = i-1
       while j >= 0 and key < array[j]:
          array[j+1] = array[j]
          j -= 1
        # inserts the key into its corrent position in the sorted part
       array[j+1] = key

fileName = 'numbers.txt'
array2 = readFile(fileName)

position = 7586

printIndex = min(position, len(array2)-1)

insertion_sort(array2)

print("At position " + str(position) + ", the value is " + str(array2[printIndex]))
