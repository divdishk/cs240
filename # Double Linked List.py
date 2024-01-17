# Double Linked List
class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

# to perform insertion sort
def insertionSort(head):
    sortedHead = None
    current = head

    while current:
        nextNode = current.next
        sortedHead = sortedInsert(sortedHead, current)
        current = nextNode

    return sortedHead

# to insert a new node into the sorted doubly linked list
def sortedInsert(head, newNode):
    current = None

    if head is None or head.data >= newNode.data:
        newNode.next = head
        if head:
            head.prev = newNode
        head = newNode
    else:
        current = head
        while current.next and current.next.data < newNode.data:
            current = current.next

        newNode.next = current.next
        if current.next:
            current.next.prev = newNode
        current.next = newNode
        newNode.prev = current

    return head

def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

def push(head, newData):
    newNode = Node(newData)
    newNode.next = head
    if head:
        head.prev = newNode
    head = newNode
    return head

def deleteFromBeginning(head):
    if head:
        newHead = head.next
        if newHead:
            newHead.prev = None
        del head
        return newHead
    return head

def deleteFromPosition(head, position):
    if position == 0:
        return deleteFromBeginning(head)

    current = head
    for _ in range(position - 1):
        if current is None or current.next is None:
            return head
        current = current.next

    if current.next:
        nextNode = current.next.next
        if nextNode:
            nextNode.prev = current
        del current.next
        current.next = nextNode

    return head

def deleteFromEnd(head):
    if head is None or head.next is None:
        del head
        return None

    current = head
    while current.next.next:
        current = current.next

    del current.next
    current.next = None

    return head

def linearSearch(head, target):
    current = head
    position = 0
    while current:
        if current.data == target:
            return position
        current = current.next
        position += 1
    return -1

def readFile(fileName):
   with open(fileName, "r") as file: # opens the file in read mode and automatically closes
      # reads each line of file
      array = [int(line.strip()) for line in file]
   return array

fileName = 'numbers-2.txt'
values = readFile(fileName)


doublyLinkedList = None
for value in values:
    doublyLinkedList = push(doublyLinkedList, value)

print("Doubly Linked List before sorting:")
printList(doublyLinkedList)

# Sorting the doubly linked list using insertion sort

sortedDoubly = insertionSort(doublyLinkedList)

print("\nDoubly Linked List after sorting:")
printList(sortedDoubly)

#eamples
sortedDoubly = deleteFromBeginning(sortedDoubly)
sortedDoubly = deleteFromPosition(sortedDoubly, 2)
sortedDoubly = deleteFromEnd(sortedDoubly)


target_value = 9727267
position = linearSearch(sortedDoubly, target_value)
print(f"\nLinear search: Element {target_value} found at position {position}")
