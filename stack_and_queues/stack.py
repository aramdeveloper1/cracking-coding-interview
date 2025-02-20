class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Pushes an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item of the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        """Returns the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.items)
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)

# print(stack.pop())  # Output: 30 (Last-In-First-Out)
# print(stack.peek()) # Output: 20 (Top of the stack)
# print(stack.is_empty()) # Output: False

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the front item of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        """Returns the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.items)

# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)

# print(queue.dequeue())  # Output: 10 (First-In-First-Out)
# print(queue.peek())     # Output: 20 (Front of the queue)
# print(queue.is_empty()) # Output: False
