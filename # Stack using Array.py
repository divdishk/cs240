# Stack using Array
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def push(self, data):
        if self.isFull():
            raise Exception("Stack is full")
        self.top += 1
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        popped_data = self.stack.pop()
        self.top -= 1
        return popped_data

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

# Example usage:
array_stack = ArrayStack(3)
array_stack.push(1)
array_stack.push(2)
array_stack.push(3)

print("Peek:", array_stack.peek())  # Output: 3
print("Pop:", array_stack.pop())    # Output: 3
print("Pop:", array_stack.pop())    # Output: 2
print("Is Empty:", array_stack.isEmpty())  # Output: False