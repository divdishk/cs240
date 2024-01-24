# Queue using an Array

class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.isFull():
            raise Exception("Queue is full")
        self.stack.append(data)
        self.rear += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        dequeuedData = self.stack[self.front]
        self.front += 1
        return dequeuedData

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.capacity

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.stack[self.rear - 1]

# Example usage:
array_queue = ArrayStack(3)
array_queue.enqueue(1)
array_queue.enqueue(2)
array_queue.enqueue(3)

print("Peek:", array_queue.peek())  
print("Dequeue:", array_queue.dequeue()) 
print("Dequeue:", array_queue.dequeue())  
print("Is Empty:", array_queue.isEmpty())  