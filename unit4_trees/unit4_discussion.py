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

        # Value represented by the node
        self.value = value

        # Direct child nodes
        self.left_node = None
        self.right_node = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # Initial root node is None
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

        # Only go recursive if there is a RootNode
        if self.root_node is None:
            self.root_node = Node(value)
        else:
            self._insert_recursive(self.root_node, value)

        """
            Insertion depends on whether a value is larger or smaller on the current node because
        BSTs are sorted collections. Whether a value ends up on the left of right side subtree
        of the current node is dependent on whether the value is less or greater than the current
        node's value. This sorting system is what allows it to be efficient for finding and storing
        values.
        """


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

        # Do not insert value if value already exists in BST
        if value == node.value:
            return

        # Insert to left side if value is less than current node's value
        if value < node.value:
            # Set value as value of left node if no left child exists
            if node.left_node is None:
                node.left_node = Node(value)
            # Recursive insert to left side subtree
            else:
                self._insert_recursive(node.left_node, value)
        # Insert to right side if value is greater than current node's value
        else:
            # Set value as value of right node if no right child exists
            if node.right_node is None:
                node.right_node = Node(value)
            # Recursive insert to right side subtree
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

        # Only go recursive if there is a RootNode
        # Value is not in BST if BST is empty
        if self.root_node is None:
            return False
        else:
            return self._search_recursive(self.root_node, value)

        """
            BST search is often more efficient than a linear search because the search for a perfect tree
        has a worst case scenario of O(logN). This is because the height of the tree is what determines
        the worst case, and the height of a tree is logN. The worst case of a BST is possible to be O(N),
        which is the worst case of a linear search, if the tree is highly skewed. This is unlikely if the
        BST was populated with random values.
        """

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Return true if value is found
        if value == node.value:
            return True

        # Search left subtree if value is less than current value
        if value < node.value:
            # Value does not exist in tree
            if node.left_node is None:
                return False
            # Search left subtree
            else:
                return self._search_recursive(node.left_node, value)
        else:
            # Value does not exist in tree
            if node.right_node is None:
                return False
            # Search right subtree
            else:
                return self._search_recursive(node.right_node, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        # Create empty list
        values = []

        # Only go recursive if there is a RootNode
        if self.root_node is not None:
            self._inorder_recursive(self.root_node, values)

        # Return Populated List
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

        # Add values in left subtree first
        if node.left_node is not None:
            self._inorder_recursive(node.left_node, values)

        # Add current values
        values.append(node.value)

        if node.right_node is not None:
            self._inorder_recursive(node.right_node, values)

        """
            This traversal produces a sorted output because the BST is constructed with the lowest value
        being in the leftmost child node and the highest value being in the rightmost child node. By printing
        the values that exist in the left child node first, then the current node's value, then the right
        child node, you get ascending order.
        """


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

    """
        A BST is efficient at reducing search space by allowing the search algorithm to
    sort through possible values without needing to directly check them. By being able to
    traverse the tree, using the current node's value being greater or less than the searched
    for value, values that exist in the tree are ruled out as being the possible value being
    checked for without directly observing the nodes. This decrease the amount of processing
    power needed to find the value.
    """

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

    """
        Traversal produces a sorted output by printing the values that occur
    leftmost on the tree first before printing out the values that occur rightmost
    on the tree. This algorithm, along with the left to right ascending order used
    when the tree is built, creates an ascending list of the values existing in
    the tree.
    """

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

    """
        This section is demonstrating the ability for the search method to locate
    a value and whether it exists in the BST. It traverses the tree, using the
    node's values to guide it, and checks whether the value is within the tree.
    If it is present in the tree, the method returns True. If not, it returns False.
    """

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

    """
        If a search occurs in an empty tree, the method immediately recognizes it does
    not have a root node, and returns false due to the tree being empty.
    """

    print(f"--Populating Tree With Duplicates--")
    data_list_edge = [ 1, 1, 2, 3, 3]
    print(f"Adding the Following Content to the BST: {data_list_edge}")
    for data in data_list_edge:
        bst_edge.insert(data)
    print(f"The BST After Populated Prints as: {bst_edge.inorder()}")

    """
        BSTs are collections of unique values, meaning if a value already exists within
    the BST, it is not stored again. When this case tries to add new values that already
    exist within the collection, they are rejected, and no addition is made.
    """


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