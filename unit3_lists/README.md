# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
    - The concepts and skills I leaned was the basic functionality and edge cases for the Python list. It was interesting seeing what the outputs were for certain cases, such as pop with an empty list or inserting at a unoccupied index. It also helped me think of real world scenarios to apply lists to.
2. What challenges did you encounter, and how did you overcome them?
    - Main challenge I encountered was a design decision for the search function, which was whether to use a try-catch implementation or a “value in list” implementation. I ended up deciding on try-catch because it had a half the processing time associated with it, as it only needed to traverse the list once.
3. How do list operations impact performance in real-world applications?
    - List operations impact performance by how long it takes to find certain values, how much memory it needs to allocate, and how many operations it takes to add/remove values. The way the list will be interacted with needs to be kept in mind as the lower implementation is added. A list that will have specific indexes referenced frequently should uses an array-based list while a list that will have its values moved around frequently should use a linked list.
