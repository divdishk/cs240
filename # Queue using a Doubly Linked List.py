# Queue using a Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        dequeuedData = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return dequeuedData

    def isEmpty(self):
        return self.head is None

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.tail.data

# Example usage:
doubly_linked_list_queue = DoublyLinkedListQueue()
doubly_linked_list_queue.enqueue(1)
doubly_linked_list_queue.enqueue(2)
doubly_linked_list_queue.enqueue(3)

print("Peek:", doubly_linked_list_queue.peek())  
print("Dequeue:", doubly_linked_list_queue.dequeue()) 
print("Dequeue:", doubly_linked_list_queue.dequeue())  
print("Is Empty:", doubly_linked_list_queue.isEmpty()) 