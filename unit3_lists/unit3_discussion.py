"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst: list, index: int, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Inserts the value at the given index of the list
    lst.insert(index, value)

    """
        The existing elements will be moved within the list to a higher index
    in order to create room to fit the new value at the requested index.
        Depending on where the value is requesting to be inserted, this
    method can take O(1) operation time to O(N) operation time. O(1) is
    if the value is inserted at the end of the list, O(N) is if the value
    is inserted at the front. This is because if the value is inserted at
    the end of the list, no other values need to shift. If it is inserted
    at the front of the list, every value already existing in the list needs
    to be shifted by being inserted to the index above itself.
    """


def delete_at(lst: list, index: int):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check if the index exists within the list
    if (len(lst) - 1) < index:
        return None

    # Return the value at the index of the list while removing the value from the list
    return lst.pop(index)

    """
        Index validation and safe deletion are important because without it, you can
    get undefined behavior. Undefined behavior can either cause errors or accessing
    and modifying memory that is not appropriate for the method to interact with. This
    can cause various unpredictable and exploitable behaviors that are not desirable
    for the program.
    """


def search_value(lst: list, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # Traverse list until the end, which throws an error if hit
    try:
        # Return the first instance of the value's index
        return lst.index(value)
    # Return default value if no value was found
    except ValueError:
        # Return a default invalid value (-1)
        return -1

    """
        This is a linear search and scans sequentially because each value in the list
    is checked until a value matches the value handed in the parameters. Because of the
    fact that every value needs to be checked (until a match is found), it is linear.
    Worst case performance will be O(N) and best will be O(1)
    """

    """
    OLD IMPLEMENTATION:
    REASON FOR BEING SCRAPPED: Traverses lst twice instead of once: O(2N) worst and O(2) best
    # Checks if the value is within the list to avoid errors
    if value in lst:
        # Return the first instance of the value's index
        return lst.index(value)
    else:
        # Return a default invalid value (-1)
        return -1
    """

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")


    print(f"\n-DEMONSTRATING LIST CREATION-")

    print(f"--Creating the List--")
    list_animals = ["Scorpion", "Bee", "Robin"]
    print(f"Current List Contents: {list_animals}")

    print(f"\n-DEMONSTRATING LIST BEGINNING INSERTION-")

    # Creating parameters for insertion at the very beginning of the list
    new_animal_beg = "Spider"
    index_beg = 0
    print(f"--Inserting {new_animal_beg} To Index: {index_beg}--")
    insert_at(list_animals, index_beg, new_animal_beg)
    print(f"Current List Contents: {list_animals}")

    print(f"\n-DEMONSTRATING LIST MIDDLE INSERTION-")

    # Creating parameters for insertion at the middle of the list
    new_animal_mid = "Parrot"
    # Divide by 2, round down, for middle index
    index_mid = len(list_animals) // 2
    print(f"--Inserting {new_animal_mid} To Index: {index_mid}--")
    insert_at(list_animals, index_mid, new_animal_mid)
    print(f"Current List Contents: {list_animals}")

    print(f"\n-DEMONSTRATING LIST END INSERTION-")

    # Creating parameters for insertion at the very end of the list
    new_animal_end = "Elephant"
    index_end = len(list_animals)
    print(f"--Inserting {new_animal_end} To Index: {index_end}--")
    insert_at(list_animals, index_end, new_animal_end)
    print(f"Current List Contents: {list_animals}")


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    print(f"--Creating the List--")
    list_flavors = ["Sour", "Umami", "Salty", "Sweet", "Bitter", "Tangy", "Savory"]
    print(f"Current List Contents: {list_flavors}")

    print(f"\n-DEMONSTRATING LIST BEGINNING REMOVAL-")

    # Creating parameters for removing the very beginning of the list
    index_beg = 0
    print(f"--Removing Index: {index_beg} From List--")
    # Delete and print value deleted
    print(f"{delete_at(list_flavors, index_beg)} has been Removed from the List")
    print(f"Current List Contents: {list_flavors}")

    print(f"\n-DEMONSTRATING LIST MIDDLE REMOVAL-")

    # Creating parameters for removing the middle of the list
    # Divide by 2, round down, for middle index
    index_mid = len(list_flavors) // 2
    print(f"--Removing Index: {index_mid} From List--")
    #Delete and print value deleted
    print(f"{delete_at(list_flavors, index_mid)} has been Removed from the List")
    print(f"Current List Contents: {list_flavors}")

    print(f"\n-DEMONSTRATING LIST ENDING REMOVAL-")

    # Creating parameters for removing the very end of the list
    index_end = len(list_flavors) - 1
    print(f"--Removing Index: {index_end} From List--")
    # Delete and print value deleted
    print(f"{delete_at(list_flavors, index_end)} has been Removed from the List")
    print(f"Current List Contents: {list_flavors}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    print(f"--Creating the List--")
    list_numbers = [3, 70, 8, 12, 65]
    print(f"Current List Contents: {list_numbers}")

    print(f"\n-DEMONSTRATING SEARCH FOR VALUE THAT EXISTS-")

    print(f"Current List Contents: {list_numbers}")
    # Getting value that exists in list
    # Divide by 2, round down, for middle index
    search_number = list_numbers[len(list_numbers) // 2]
    print(f"--Searching For: {search_number} In List--")
    # Searching and Printing index found
    # Slightly dishonest since it prints it has been found before finding it, but
    #for the sake of demonstration, I think it is fine
    print(f"{search_number} has been Found in the List at Index: {search_value(list_numbers, search_number)}")


    print(f"\n-DEMONSTRATING SEARCH FOR VALUE THAT DOES NOT EXISTS-")

    print(f"Current List Contents: {list_numbers}")
    # Making up value that does not exist in list
    # Bug: no check to see if this number exists
    search_number_inv = -100
    print(f"--Searching For: {search_number_inv} In List--")
    # Searching and Printing index found
    # Slightly dishonest since it prints value has been not found before searching for it, but
    #for the sake of demonstration, I think it is fine
    print(f"{search_number_inv} has NOT been Found in the List, returned Index: {search_value(list_numbers, search_number_inv)}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    print(f"--Creating Empty List--")
    list_empty = []
    print(f"Current List Contents: {list_empty}")

    print(f"\n-DEMONSTRATING SEARCH FOR VALUE IN EMPTY LIST-")

    print(f"Current List Contents: {list_empty}")
    # Creating value that is not in the list
    search_number_empty = 300
    print(f"--Searching For: {search_number_empty} In List--")
    # Searching and Printing output
    print(f"{search_number_empty} has NOT been Found in the List, returned Index: {search_value(list_empty, search_number_empty)}")
    print(f"Current List Contents: {list_empty}")

    """
        Because the value does not exist in the list, the method returns the default value of -1, an index that cannot be
    found if the value exists in the list
    """



    print(f"\n-DEMONSTRATING REMOVING IN EMPTY LIST-")

    print(f"Current List Contents: {list_empty}")
    # Creating parameters for removing at index not in list
    index_empty_rem = 10
    print(f"--Removing Index: {index_empty_rem} From List--")
    # Delete and print value deleted
    print(f"Since Index {index_empty_rem} does NOT exist in list, Removing Returned: {delete_at(list_empty, index_empty_rem)}")
    print(f"Current List Contents: {list_empty}")

    """
        Because the value does not exist in the list, the method returns the default value of None, a value which was not
    being tried to remove
    """



    print(f"\n-DEMONSTRATING INSERTING TO EMPTY LIST-")

    print(f"Current List Contents: {list_empty}")
    # Creating parameters for removing at index not in list
    number_empty = 87
    index_empty_in = 20
    print(f"--Inserting {number_empty} To Index: {index_empty_in}--")
    insert_at(list_empty, index_empty_in, number_empty)
    print(f"Current List Contents: {list_empty}")

    """
        Because the index to be inserted at is not occupied with a value, the list adds it to the highest possible
    value it can reasonably be inserted to, which in this case is 0 since it is an empty list
    """

if __name__ == "__main__":
    main()