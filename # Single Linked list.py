# Single Linked list

# class to represent each element in the linked list
class Node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None

# to perform insertion sort 
def insertionSort(head):
    sortedHead = None
    current = head

    while(current != None):
        nextNode = current.next
        sortedHead = sortedInsert(sortedHead, current)
        current = nextNode
    return sortedHead

# to insert a new node into the sorted linked list
def sortedInsert(head, newNode):
    current = None
    if (head == None or (head).data >= newNode.data):
        newNode.next = head
        head = newNode
    else:
        current = head
        while (current.next != None and current.next.data < newNode.data):
            current = current.next
   
        newNode.next = current.next
        current.next = newNode
    return head

# to print linked list
def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

# to insert a new node at the beginning of the linked list
def push(head, newData):
    newNode = Node(newData)
    newNode.next = head
    head = newNode
    return head

# to delete the first node
def deleteFromBeginning(head):
    if head:
        newHead = head.next
        del head
        return newHead
    return head

# to delete a node at a specific position
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
        del current.next
        current.next = nextNode

    return head

# to delete the last node
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

linkedList = None
for value in values:
    linkedList = push(linkedList, value)

print("Linked List before sorting: ")
printList(linkedList)

sortedList = insertionSort(linkedList)

print("\nLinked List after sorting: ")
printList(sortedList)

#examples
sortedList = deleteFromBeginning(sortedList)
sortedList = deleteFromPosition(sortedList, 10)
sortedList = deleteFromEnd(sortedList)

# linear search
target_value = 9810169
position = linearSearch(sortedList, target_value)
print(f"\nLinear search: Element {target_value} found at position {position}")
