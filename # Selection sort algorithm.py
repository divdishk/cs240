# Selection sort algorithm 
# Divdish Kaur
# CS 240

def readFile(fileName): 
   with open(fileName, "r") as file: # opens the file in read mode and automatically closes
      # reads each line of file
      array = [int(line.strip()) for line in file]
   return array

def selectionSort(array):
   # iterates through each element in array
   for i in range(len(array)):
      # assumes the current index is the min
      minIndex = i
      #iterates through the remaining elements to find min
      for j in range(i+1, len(array)):
         if array[j] < array[minIndex]:
            minIndex = j
      # swaps the current element with minimum element
      array[i], array[minIndex] = array[minIndex], array[i]
   

fileName = 'numbers.txt'
array2 = readFile(fileName)

selectionSort(array2)

position = 7586

printIndex = min(position, len(array2)-1) #index doesn't go out of bound
print("At position " + str(position) + ", the value is " + str(array2[printIndex]))