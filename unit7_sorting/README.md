# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
    - The concepts I learned within this assignment were learning how to write a Bubble Sort and Merge Sort Algorithm in Python. I had to write Bubble Sort for the Unit 7 lab so translating to Python was mostly the same logic. Merge Sort was a different situation, as I have never wrote a Merge Sort algorithm before. I used the book as guidance for the processes that go into merge sort while trying to make the algorithm my own.
2. What challenges did you encounter, and how did you overcome them?
    - The main challenge I encountered in this was a small amount of logic inside of the Merge Sort algorithm that I did not realize I was not updating. The bug was that the merge_sort() method was not taking the return of merge() for its lower and higher halves, making it so that the recursive returning was not happening. It was also somewhat challenging thinking of the second real life scenario and how to implement it. I sorted a Dictionary inside of that example, but since I am not implementing interfaces in my algorithms as inputs, I had to do a lot of extra exterior operations to get a new Dictionary that reflected the sorting from Merge Sort.
3. Compare and contrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.
    - For the most part, Merge Sort is better than Bubble Sort. This is due to the fact that Merge Sort scales significantly better with large data sets than Bubble Sort, as Bubble Sort has a runtime complexity of O(N^2) while Merge Sort has a runtime complexity of O(N(logN)). The massive difference in processing that this takes in large data sets is shown in my large dataset case. For much smaller data sets, Bubble Sort actually seems to be more efficient than Merge Sort. So if you know you will be working with a small dataset, and you have these two algorithms to choose from, go with Bubble Sort. Otherwise, and in most cases, use Merge Sort.