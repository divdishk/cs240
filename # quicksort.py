# quicksort
def quickSort(array, low, high):
    if low < high:
        # finds the index of the pivot element (<pivot on left and >pivot on right)
        indexPivot = partition(array, low, high)
        # recursively sorts the subarrays on the left and right of the pivot
        quickSort(array, low, indexPivot - 1)
        quickSort(array, indexPivot + 1, high)

def partition(array, low, high):
    # last element as pivot
    pivot = array[high]

    indexPivot = low - 1

    # iterates through elements and rearranges them to the pivot
    for i in range(low, high):
        if array[i] <= pivot:
            # swaps elements if they are smaller than or equal to the pivot
            array[i], array[indexPivot + 1] = array[indexPivot + 1], array[i]
            indexPivot += 1

    #swaps into the correct position
    array[high], array[indexPivot + 1] = array[indexPivot + 1], array[high]

    return indexPivot + 1


array = [38, 27, 43, 3, 9, 82, 10]
quickSort(array, 0, len(array) - 1)
print("Sorted array:", array)
