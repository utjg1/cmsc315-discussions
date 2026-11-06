# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   - The concepts I learned within this assignment were learning how to interface with the Python Dictionary and some of the nuances of its functionality and below the hood workings. I also thought of practical uses for Hash Tables.
2. What challenges did you encounter, and how did you overcome them?
   - The main challenge I ran into was deciding the best times to show a Hash Table. I knew internally when the Hash Table would and would not be updated, but I had to think about when to demonstrate that. I found myself presenting the state of the Hash Table after nearly demonstration, which I do not necessarily think is wrong. I Think it could also demonstrate to the reader when the Hash Table is and is not updating.
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
   - Hash Tables are similar to other data collections except piece of data is expected to have two parts, a key and a value. The key is what is used by the Hash table to decide where to store data and where to retrieve it from, while the value is the data stored with the associated key. Since a Hash Table uses a hashing algorithm for finding and storing keys, this algorithm does not always have unique outputs for every key. This leads to hash collisions, were the data being searched for or stored finds that the expected location of the data contains not the data it is looking for but instead data indicating that the data it is looking for could be at another location in its memory. This hash collision causes the same algorithm to be ran multiple times with slight alterations when trying to find the key value pair associated with the key. A Hash Table can improve efficiency by reducing hash collisions, and this can be done by expanding the existing space of where data can exist. This larger set of possible data locations makes it less likely that the hashing algorithm will create the same hash for two separate keys, leading to lower collisions, leading to less algorithm processing, leading to higher efficiency.