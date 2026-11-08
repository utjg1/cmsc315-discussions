"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Edge case for empty graph
    if not graph:
        return []

    # Edge case for start not in graph
    if not (start in graph):
        return []

    # Initialize visited with first value
    visited = [start]
    queue = deque()

    # Add vertices connected to starting vertex
    for vertex in graph[start]:
        queue.append(vertex)

    # Loop through in BFS order
    while queue:
        # Pop next value to visit
        cur_vertex = queue.popleft()

        # Iterate through neighboring vertexes
        for vertex in graph[cur_vertex]:
            # Only add to queue if not already in queue and not visited
            if not((vertex in queue) or (vertex in visited)):
                queue.append(vertex)

        # Add current index to visited
        visited.append(cur_vertex)

    # Return BFS order list
    return visited


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    print(f"--Creating Adjacency List Graph for a Subway--")
    stops = ["Apple Lane", "Berryvillage", "Cherry Woods", "Decant Valley", "Eggland", "Frogplace"]
    connections = [("Apple Lane","Berryvillage"),
             ("Apple Lane","Cherry Woods"),
             ("Berryvillage","Cherry Woods"),
             ("Cherry Woods","Decant Valley"),
             ("Cherry Woods","Eggland"),
             ("Decant Valley", "Eggland"),
             ("Eggland","Frogplace")]
    subway_connections = {}
    print(f"Building Graph...")

    # Populate graph with vertices
    for vertex in stops:
        subway_connections.update({vertex: []})

    # Populate graph with edges
    for edge in connections:
        # Only populate with edge if edge exists in vertices
        if (edge[0] in stops) and (edge[1] in stops):
            # Only add to index 0's list if index 1 does not exist in it
            if not (edge[1] in subway_connections[edge[0]]):
                subway_connections[edge[0]].append(edge[1])
            # Only add to index 1's list if index 0 does not exist in it
            if not (edge[0] in subway_connections[edge[1]]):
                subway_connections[edge[1]].append(edge[0])

    print(f"Displaying Finished Graph:")
    for stop in subway_connections:
        print(f"{stop}:{subway_connections[stop]}")

    """
    The nodes and edges of the graph I decided to make, each vertex represents the stop in a subway line and each
    edge represents a connection from stop to stop. Real world space is a commonly represented scenario by graphs
    as it maps on intuitively. For the sake of easier reading, I also started each stop with letters descending
    from A to F.
    """


    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    print(f"--Demonstrating BFS Algorithm--")
    start = stops[0]
    print(f"Traversing Graph with BFS Using {start} as the Starting Vertex...")
    traversed_order = bfs(subway_connections, start)
    print(f"Traversal Finished! Order Found: {traversed_order}")

    print(f"--Demonstrating BFS Algorithm With Altered Graph--")
    subway_connections.update({"Y Palace": ["Apple Lane", "Cherry Woods"]})
    subway_connections["Apple Lane"].append("Y Palace")
    subway_connections["Cherry Woods"].append("Y Palace")
    print(f"Graph Has Been Altered to Become:")
    for stop in subway_connections:
        print(f"{stop}:{subway_connections[stop]}")
    start = stops[0]
    print(f"Traversing Graph with BFS Using {start} as the Starting Vertex...")
    traversed_order_altered = bfs(subway_connections, start)
    print(f"Traversal Finished! Order Found: {traversed_order_altered}")

    """
    BFS traverses vertexes in order of how many connections they take to reach from the starting
    vertex. The vertices with the least amount of necessary connections are checked first, then
    the second most connections, and so on. This means the trend of the BFS visited order will
    have the lowest amount of connections displayed at the start, and highest at the end.
    """

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print(f"--Demonstrating Starting From a Different Node--")
    start_altered = stops[1]
    print(f"Traversing Graph with BFS Using {start_altered} as the Starting Vertex...")
    traversed_order_start_altered= bfs(subway_connections, start_altered)
    print(f"Traversal Finished! Order Found: {traversed_order_start_altered}")

    """
    BFS is dependent on the starting vertex when determining the order of the visited vertices. When
    the starting node is changed, the BFS changes, and depending how far away the starting vertex is,
    the resulting visited list can be wildly different.
    """

    print(f"--Demonstrating Disconnected Graph Behavior--")
    subway_connections.update({"Zero Land": []})
    print(f"Added Vertex Z with No Connections to Graph")
    start_altered = stops[1]
    print(f"Traversing Graph with BFS Using {start_altered} as the Starting Vertex...")
    traversed_order_start_altered= bfs(subway_connections, start_altered)
    print(f"Traversal Finished! Order Found: {traversed_order_start_altered}")
    start_isolated = "Zero Land"
    print(f"Traversing Graph with BFS Using {start_isolated} as the Starting Vertex...")
    traversed_order_start_isolated= bfs(subway_connections, start_isolated)
    print(f"Traversal Finished! Order Found: {traversed_order_start_isolated}")

    """
    Disconnected vertices do not have an edge to be traversed through to be reached, or have edges
    to traverse from. This means that BFS applied to vertices with no possible connection will not
    be displayed in the visited list. For an isolated vertex, if BFS is applied to it, the only
    visited vertex will be itself.
    """


if __name__ == "__main__":
    main()