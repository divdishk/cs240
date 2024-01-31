# quicksort
def readFile(fileName):
   with open(fileName, "r") as file: # opens the file in read mode and automatically closes
      # reads each line of file
      array = [int(line.strip()) for line in file]
   return array

def quickSort(array, low, high):
    if low < high:
        indexPivot = partition(array, low, high)
        quickSort(array, low, indexPivot - 1)
        quickSort(array, indexPivot + 1, high)

def partition(array, low, high):

    pivot = array[high]

    indexPivot = low - 1

    for i in range(low, high):
        if array[i] <= pivot:

            array[i], array[indexPivot + 1] = array[indexPivot + 1], array[i]
            indexPivot += 1


    array[high], array[indexPivot + 1] = array[indexPivot + 1], array[high]

    return indexPivot + 1


fileName = "numbers-4.txt"
fileArray = readFile(fileName)
quickSort(fileArray, 0, len(fileArray)-1)
print("Sorted array: ", fileArray)