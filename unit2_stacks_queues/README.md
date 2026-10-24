# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   - During this assignment, I learned the general behavior of stacks and queues. They are both data holding objects but the order at which they provide that data is different. LIFO for stacks, FIFO for queues.
2. What challenges did you encounter, and how did you overcome them?
   - The major challenges I approached when making this were design decisions and demonstration decisions. Deciding whether I wanted to throw or return a default value when peeking/fronting or popping/dequeuing from an empty object took me a moment but I ultimately decided on throwing. I think both ways are valid, but since I think that empty objects are a valid input, I thought throwing was a meaningfully different outcome compared to getting a default. I also had to think about how much demonstration was necessary to show all of the stack/queues functionality by thinking of the different ways I can interact with it, such as meaningfully demonstrating peek/front.
3. Explain the differences between stacks and queues as this relates to real-world applications.
   - The differences in stacks and queues as it relates to real implementation, at least for how they were built for this assignment, mostly comes down to whether you want LIFO or FIFO behavior. I chose a stack for playing cards since you tend to add and pull from the top of a deck, and I chose a queue a doctor’s waiting room since you tend to attend patients who came in before the other patients first. There is probably more implementation needed for a wholistic representation of these situations (shuffling a deck, assessing patient urgency), but for a school assignment, I think the demonstration shows my understanding of the concept.
