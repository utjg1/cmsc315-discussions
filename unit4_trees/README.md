# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   - The concepts and skills I leaned was the basic functionality and edge cases for how a Binary Search Tree works and utilizing recursion to search data. It was also interesting thinking of my own practical example of how a basic search for string data could be used with a BST.
2. What challenges did you encounter, and how did you overcome them?
   - The major challenges I encountered when creating my BST had to do with some unexpected outputs. There was a moment where I was seeing my search method return with None instead of True or False. I was confused, went back to observe my implementation, and realized I was not returning a value for my recursive steps. Was a small problem, but one I am not used to facing since I primarily program in languages were a defined return type is required on defining a method. Python is not like that, so getting None was shocking when I was expecting a binary output.
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
   - BST behavior works differently compared to other kinds of data structures such as lists and linked lists by being constructed in such a way that allows the search algorithm to find values without needing to check every node. This is because the BST has multiple branches that are created dependent on the child node’s value compared to the parent. This allows a search algorithm to rule out large sections of the tree based on the current value in the node it is observing and the value it is searching for. This is much a much more efficient search algorithm than what a list or linked list provides, as their worst case search is O(N) and a perfect BST has a worst case of O(logN). Even when the BST is highly skewed, it is only has as bad of a worst case of O(N), and that is an unlikely tree to construct when handed random data.