"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""
import queue
from collections import deque
from logging import exception


class Stack:
    def __init__(self):
        # This list is the only thing I need to initialize at the beginning of a stack as it will
        # keep track of the order of my data and can be dynamically resized
        self.list = []

    def push(self, value):
        # Adds a value to the end of my stack's list, which is where I pop from
        self.list.append(value)

    def pop(self):
        # Throws an exception if the list is empty to catch undefined returns
        if not self.list:
            raise IndexError("Stack Pop while Empty!")

        # Returns the value at the end of the list, which is the most recently added value
        # The pop method also removes the value at the index from the list
        return self.list.pop(len(self.list) - 1)

    def peek(self):
        # Throws an exception if the list is empty to catch undefined returns
        if not self.list:
            raise IndexError("Stack Peek while Empty!")

        # Returns the value at the end of the list, which is the most recently added value
        # Since this is just returning the value at the last index, it is not removing it
        return self.list[len(self.list) - 1]

    def is_empty(self):
        # Returns whether the internal list is empty
        return not self.list


class Queue:
    def __init__(self):
        # The deque object has the implementation I will need for creating a Queue
        self.queue = deque()

    def enqueue(self, value):
        # Adds an object to the beginning of the queue, the furthest position away
        # from being popped
        self.queue.appendleft(value)

    def dequeue(self):
        # Throws an exception if the deque is empty to catch undefined returns
        if not self.queue:
            raise IndexError("Queue Dequeue while Empty!")

        # Take the object from the end of the deque, the furthest to the right value,
        # remove it from the deque and return it
        return self.queue.pop()

    def front(self):
        # Throws an exception if the list is empty to catch undefined returns
        if not self.queue:
            raise IndexError("Queue Front while Empty!")

        # Returns at the object at the end of the deque without removing it
        return self.queue[len(self.queue) - 1]

    def is_empty(self):
        # Returns whether the deque is empty
        return not self.queue


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")



    print(f"\n-DEMONSTRATING LIFO BEHAVIOR IN STACK-")

    print(f"--Creating the Stack Object--")
    s = Stack()
    print(f"Current Stack Contents: {s.list}")

    print(f"--Pushing Values to Stack--")
    for i in range(4):
        print(f"Pushing {i} to Stack")
        s.push(i)
        print(f"Current Stack Contents: {s.list}")

    print(f"--Popping Values from Stack--")
    while not s.is_empty():
        print(f"{s.pop()} Popped from Stack")
        print(f"Current Stack Contents: {s.list}")

    print(f"-ENDING LIFO BEHAVIOR IN STACK-")



    print(f"\n-DEMONSTRATING PEEK VS POP BEHAVIOR IN STACK-")

    print(f"--Creating the Stack Object--")
    s = Stack()
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"--Pushing Object to Stack--")
    test_value = "Penguin"
    print(f"Pushing {test_value} to Stack")
    s.push(test_value)
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"--Peeking Object in Stack--")
    print(f"{s.peek()} Peeked from Stack")
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"--Popping Value from Stack--")
    print(f"{s.pop()} Popped from Stack")
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"-ENDING PEEK VS POP BEHAVIOR IN STACK-")



    print(f"\n-DEMONSTRATING POP ON EMPTY STACK-")

    print(f"--Creating the Stack Object--")
    s = Stack()
    print(f"Current Stack Contents: {s.list}")

    print(f"--Popping from Empty Stack--")
    try:
        # Expected to throw an Error
        s.pop()
    except Exception as e:
        print(f"Expected Exception Has Been Thrown: {e}")

    print(f"-ENDING EMPTY POP BEHAVIOR IN STACK-")



    print(f"\n-DEMONSTRATING PEEK ON EMPTY STACK-")

    print(f"--Creating the Stack Object--")
    s = Stack()
    print(f"Current Stack Contents: {s.list}")

    print(f"--Peeking from Empty Stack--")
    try:
        # Expected to throw an Error
        s.peek()
    except Exception as e:
        print(f"Expected Exception Has Been Thrown: {e}")

    print(f"-ENDING EMPTY PEEK BEHAVIOR IN STACK-")



    print(f"\n-DEMONSTRATING STACK BECOMES EMPTY AFTER REMOVAL-")

    print(f"--Creating the Stack Object--")
    s = Stack()
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"--Pushing Object to Stack--")
    test_value = "Bunny"
    print(f"Pushing {test_value} to Stack")
    s.push(test_value)
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"--Popping Value from Stack--")
    print(f"{s.pop()} Popped from Stack")
    print(f"Current Stack Contents: {s.list}")
    print(f"Stack is Empty: {s.is_empty()}")

    print(f"-ENDING STACK BECOMES EMPTY AFTER REMOVAL BEHAVIOR-")



    # ===============================
    # QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.


    print("\n=== QUEUE DEMO ===")

    print(f"\n-DEMONSTRATING FIFO BEHAVIOR IN QUEUE-")

    print(f"--Creating the Queue Object--")
    q = Queue()
    print(f"Current Queue Contents: {q.queue}")

    print(f"--Enqueueing Values to Queue--")
    for i in range(4):
        print(f"Enqueue {i} to Queue")
        q.enqueue(i)
        print(f"Current Queue Contents: {q.queue}")

    print(f"--Dequeueing Values from Queue--")
    while not q.is_empty():
        print(f"{q.dequeue()} Dequeued from Queue")
        print(f"Current Queue Contents: {q.queue}")

    print(f"-ENDING FIFO BEHAVIOR IN QUEUE-")



    print(f"\n-DEMONSTRATING DEQUEUE VS FRONT BEHAVIOR IN QUEUE-")

    print(f"--Creating the Queue Object--")
    q = Queue()
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"--Enqueuing Object to Queue--")
    test_value = "Elk"
    print(f"Enqueuing {test_value} to Queue")
    q.enqueue(test_value)
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"--Fronting Object in Queue--")
    print(f"{q.front()} Fronted from Queue")
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"--Dequeueing Value from Queue--")
    print(f"{q.dequeue()} Dequeued from Queue")
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"-ENDING DEQUEUE VS FRONT BEHAVIOR IN QUEUE-")



    print(f"\n-DEMONSTRATING DEQUEUE ON EMPTY QUEUE-")

    print(f"--Creating the Queue Object--")
    q = Queue()
    print(f"Current Queue Contents: {q.queue}")

    print(f"--Dequeuing from Empty Queue--")
    try:
        # Expected to throw an Error
        q.dequeue()
    except Exception as e:
        print(f"Expected Exception Has Been Thrown: {e}")

    print(f"-ENDING EMPTY DEQUEUE BEHAVIOR IN QUEUE-")


    print(f"\n-DEMONSTRATING FRONT ON EMPTY QUEUE-")

    print(f"--Creating the Queue Object--")
    q = Queue()
    print(f"Current Queue Contents: {q.queue}")

    print(f"--Fronting from Empty Queue--")
    try:
        # Expected to throw an Error
        q.front()
    except Exception as e:
        print(f"Expected Exception Has Been Thrown: {e}")

    print(f"-ENDING EMPTY FRONT BEHAVIOR IN QUEUE-")


    print(f"\n-DEMONSTRATING QUEUE BECOMES EMPTY AFTER REMOVAL-")

    print(f"--Creating the Queue Object--")
    q = Queue()
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"--Enqueueing Object to Queue--")
    test_value = "Fox"
    print(f"Enqueueing {test_value} to Queue")
    q.enqueue(test_value)
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"--Dequeueing Value from Queue--")
    print(f"{q.dequeue()} Dequeued from Queue")
    print(f"Current Queue Contents: {q.queue}")
    print(f"Queue is Empty: {q.is_empty()}")

    print(f"-ENDING STACK BECOMES EMPTY AFTER REMOVAL BEHAVIOR-")

if __name__ == "__main__":
    main()
