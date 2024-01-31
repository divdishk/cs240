#mergeSort

def mergeSort(array):
	if len(array) <= 1: # base case
		return array
	
	# middle index
	mid = len(array)//2
	# splits array into left and right
	left = array[:mid]
	right = array[mid:]
	
	# recursively sorts both left and right
	mergeSort(left)
	mergeSort(right)

	return mergedArr(left, right)


def mergedArr(left, right):
	result = []
	indexL = 0
	indexR = 0

	# merges left and right sides by comparing elements
	while indexL < len(left) and indexR < len(right):
		if left[indexL] <= right[indexR]:
			result.append(left[indexL])
			indexL += 1
		else:
			result.append(right[indexR])
			indexR += 1
	# appends any remaining elements from left and right
	result.extend(left[indexL:])
	result.extend(right[indexR:])
	return result

array = [38, 27, 43, 3, 9, 82, 10]
sortedArray = mergeSort(array)
print("Sorted array:", sortedArray)
