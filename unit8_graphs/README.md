# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
    - The concepts and skills I learned in this assignment were learning how to create a graph using vertices and edges long with creating the BFS algorithm. I also learned of some practical uses for graphs along with demonstrating how small changes can greatly affect the BFS’s return with the order of visited vertices.
2. What challenges did you encounter, and how did you overcome them?
    - The main challenge I encountered in this was deciding whether I should add vertices to the queue within BFS if they already existed in the queue. That was the way I approached the lab, but I felt like it was not necessary. I thought about it for a while and made some small edits to see if it would work, and while I do not think you need to make sure the queue exclusively contains one of each vertex to visit, I decided to keep my old design since it worked.
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.
    - BFS and DFS are both search algorithms used for traversing graphs, but BFS prioritizes the vertexes closest to the start while DFS prioritizes the vertexes farthest away from the start. When you would use BFS is when the path is relatively close to the start while DFS is better for being memory efficient as memory of vertexes to visit is removed earlier than with BFS. BFS could be better for representing a bus with only a few stops while DFS could be better for pathfinding in videogames due to this memory management detail.

