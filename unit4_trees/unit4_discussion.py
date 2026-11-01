"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value

        self.left_node = None
        self.right_node = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        self.root_node = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        if self.root_node is None:
            self.root_node = Node(value)
        else:
            self._insert_recursive(self.root_node, value)


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        if value == node.value:
            return

        if value < node.value:
            if node.left_node is None:
                node.left_node = Node(value)
            else:
                self._insert_recursive(node.left_node, value)
        else:
            if node.right_node is None:
                node.right_node = Node(value)
            else:
                self._insert_recursive(node.right_node, value)

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        if self.root_node is None:
            return False
        else:
            return self._search_recursive(self.root_node, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        if value == node.value:
            return True

        if value < node.value:
            if node.left_node is None:
                return False
            else:
                return self._search_recursive(node.left_node, value)
        else:
            if node.right_node is None:
                return False
            else:
                return self._search_recursive(node.right_node, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []

        if self.root_node is not None:
            self._inorder_recursive(self.root_node, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node.left_node is not None:
            self._inorder_recursive(node.left_node, values)

        values.append(node.value)

        if node.right_node is not None:
            self._inorder_recursive(node.right_node, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    print(f"--Creating the Tree--")
    bst = BST()
    print(f"New BST Created with Content: {bst.inorder()}")

    print(f"--Populating the Tree--")
    data_list = [ 12, 10, 90, 1, 8, 17, 9]
    print(f"Adding the Following Content to the BST: {data_list}")
    for data in data_list:
        bst.insert(data)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    print(f"--Displaying the Tree--")
    print(f"The BST After Populated Prints as: {bst.inorder()}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    print(f"--Demonstrating Existing Value Search--")
    exist1 = 10
    print(f"Searching for {exist1} in the BST Returns: {bst.search(exist1)}")
    exist2 = 90
    print(f"Searching for {exist2} in the BST Returns: {bst.search(exist2)}")

    print(f"--Demonstrating Non-Existing Value Search--")
    exist3 = 2
    print(f"Searching for {exist3} in the BST Returns: {bst.search(exist3)}")
    exist4 = 1000
    print(f"Searching for {exist4} in the BST Returns: {bst.search(exist4)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    print(f"--Creating Edge Case Tree--")
    bst_edge = BST()
    print(f"New BST Created with Content: {bst_edge.inorder()}")

    print(f"--Searching Empty Tree--")
    exist5 = 25
    print(f"Searching for {exist5} in the BST Returns: {bst_edge.search(exist5)}")

    print(f"--Populating Tree With Duplicates--")
    data_list_edge = [ 1, 1, 2, 3, 3]
    print(f"Adding the Following Content to the BST: {data_list_edge}")
    for data in data_list_edge:
        bst_edge.insert(data)
    print(f"The BST After Populated Prints as: {bst_edge.inorder()}")



    # ==========================================
    # REAL WORLD SCENARIO: BIRD DATABASE
    # ==========================================

    print("\n=== REAL WORLD SCENARIO: HIGHWAY SIMULATION ===")

    print(f"--Creating Bird Database--")
    bird_database = BST()
    print(f"New Bird Database Created: {bird_database.inorder()}")

    print(f"--Populating Bird Database--")
    bird_list = [ "Crow", "Canary", "Parrot", "Albatross", "Pip", "Ostrich", "Roadrunner"]
    print(f"Adding the Following Birds to the Bird Database: {bird_list}")
    for bird in bird_list:
        bird_database.insert(bird)

    print(f"--Displaying Bird Database--")
    print(f"The Bird Database contains: {bird_database.inorder()}")

    print(f"--Searching Within Bird Database--")
    bird1 = "Parrot"
    print(f"Searching for {bird1} in the Bird Database Returns: {bird_database.search(bird1)}")
    bird2 = "Seagull"
    print(f"Searching for {bird2} in the Bird Database Returns: {bird_database.search(bird2)}")

if __name__ == "__main__":
    main()