# hw 7
class SearchAndSortHeap:
    def __init__(self):
        self.heap = [] # intializes an empty list to store heap elements
        self.size = 0 # size of heap = 0

    def parent(self, i):
        return (i - 1) // 2 # calculates the index of the parent node

    def leftChild(self, i):
        return 2 * i + 1 # calculates the index of left child node

    def rightChild(self, i):
        return 2 * i + 2 # calulates index of right child node

    def heapifyUp(self, i):
        # moves the element up the heap until the heap property is satisfied
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def heapifyDown(self, i):
        # moves the element down the heap until the heap property is satisfied
        maxIndex = i
        l = self.leftChild(i)
        if l < self.size and self.heap[l] > self.heap[maxIndex]:
            maxIndex = l
        r = self.rightChild(i)
        if r < self.size and self.heap[r] > self.heap[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self.heap[i], self.heap[maxIndex] = self.heap[maxIndex], self.heap[i]
            self.heapifyDown(maxIndex)

    def insert(self, value):
        # inserts a new element into the heap
        self.heap.append(value)
        self.size += 1
        self.heapifyUp(self.size - 1)

    def extractMax(self):
        # removes and returns the max element from the heap
        if self.size == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return root

    def search(self, value):
        # search for a value in heap
        return value in self.heap

    def heapSort(self):
        # sorts elements of the heap using the heap sort
        sortedArray = []
        while self.size > 0:
            maxVal = self.extractMax()
            sortedArray.insert(0, maxVal)
        return sortedArray


heap = SearchAndSortHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.insert(10)

print("Heap after insertion:", heap.heap)
print("Searching for value 8:", heap.search(8))
print("Sorted array:", heap.heapSort())
