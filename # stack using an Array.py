# stack using an Array

class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.isFull():
            raise Exception("Stack is full")
        self.stack.append(data)
        self.rear += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        dequeuedData = self.stack[self.front]
        self.front += 1
        return dequeuedData

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.capacity

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.rear - 1]

# Example usage:
array_stack = ArrayStack(3)
array_stack.enqueue(1)
array_stack.enqueue(2)
array_stack.enqueue(3)

print("Peek:", array_stack.peek())  # Output: 3
print("Dequeue:", array_stack.dequeue())  # Output: 1
print("Dequeue:", array_stack.dequeue())  # Output: 2
print("Is Empty:", array_stack.isEmpty())  # Output: False
