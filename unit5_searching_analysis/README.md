# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
    - The main concepts and skills I learned while writing this assignment was some basic performance analysis in python. I knew logically that Binary Search was significantly faster than Linear Search on large datasets, but being able to write and see that in numbers was a new experience. I have not done that before for my programing projects.
2. What challenges did you encounter, and how did you overcome them?
    - The challenges I encountered when writing this were mostly in trying to demonstrate the algorithms rather than writing them. I had some experience writing very similar code for the lab, this was just a more in-depth demonstration of it. One of the things I had to learn was writing large datasets in python, as I was curious how to do it cleanly without a for-loop. Another challenge was thinking of a real life example of pre-sorted lists. The book with missing pages I thought of seemed to be an interesting idea for demonstrating it.
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
    - The biggest reason to use Linear Search over Binary Search is when you are searching over unsorted data sets. While Binary Search is significantly faster in most cases than Linear Search, Binary Search only works when the data is sorted. So if the data is unsorted and is going to stay unsorted, you cannot apply Binary Search. An example of when it will not make sense to sort the data and then use Binary Search is when it is data you will only reference once or twice. If you have a program that receives a message, and the goal is to see if a large unsorted collection within this message contains a value just once, it does not make sense to sort it and then use Binary Search. In that case, you should just use a Linear Search. If for some reason you will be looking through this large collection multiple times, it may make sense to sort the collection and then apply multiple Binary Searches.