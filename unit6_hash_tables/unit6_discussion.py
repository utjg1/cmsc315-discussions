"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    print(f"--Creating New Dictionary--")
    dict = {}
    print(f"Dictionary Created with Content: {dict}")

    print(f"--Adding Key Value Pairs to Dictionary--")
    key_list = ["Monkey", "Giraffe", "Rhino", "Piranha", "Tiger"]
    value_list = [12, 3, 4, 45, 2]
    for i in range(len(key_list)):
        print(f"Adding Key Value Pair to Dictionary: {key_list[i]}:{value_list[i]}")
        dict.update({key_list[i]: value_list[i]})

    print(f"--Displaying to Dictionary After Addition--")
    print(f"Dictionary After Adding Content: {dict}")

    """
    Dictionaries in Python behave like a Hash Table because they are key value pair
    data structures. The Dictionary object also uses hashing algorithms to keep track
    of key value pair positions, same as Hast Tables, but Python's hash table data
    structures are atypical due to being highly optimized, trying to approach the
    average O(1) for data retrieval.
    """

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    print(f"--Retrieving Key Value Pairs From Dictionary--")
    key1 = key_list[1]
    key2 = key_list[4]
    print(f"Querying the Dictionary for: {key1}...")
    print(f"Value Found to be Paired with {key1}: {dict.get(key1)}")
    print(f"Querying the Dictionary for: {key2}...")
    print(f"Value Found to be Paired with {key2}: {dict.get(key2)}")

    """
    The way lookups work in Hash Tables are that a key is taken by the Hast Table
    and ran through the Hast Table's hashing algorithm to find the expected location
    of the key value pair of the key within the Hash Table's internal memory. If the
    key value pair is not at the expected location for the given key, the algorithm
    will run again, this time with the iteration associated with the number of attempts
    to find the next expected location for the key value pair. This process continues
    until the key value pair is found or the expected location contains data indicating
    that it is not possible for they to have been stored.
    """

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print(f"--Displaying to Dictionary Before Modification--")
    print(f"Dictionary Before Modification: {dict}")

    print(f"--Updating Key Value Pair in Dictionary--")
    key_to_update = key_list[3]
    new_value = value_list[3] + 5
    print(f"Querying the Dictionary for: {key_to_update}...")
    print(f"Value Found to be Paired with {key_to_update}: {dict.get(key_to_update)}")
    print(f"Updating the Key {key_to_update} to be Paired with Value: {new_value}...")
    dict.update({key_to_update: new_value})
    print(f"Querying the Dictionary for: {key_to_update}...")
    print(f"Value Found to be Paired with {key_to_update}: {dict.get(key_to_update)}")

    print(f"--Displaying to Dictionary After Modification--")
    print(f"Dictionary After Modification: {dict}")

    """
    When an existing key is assigned a new value, the key value pair that existed within
    the Dictionary is modified to contain the same key but a new value. This means the old
    value is lost and there is not more data allocated for the key value pair update.
    """

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"--Displaying to Dictionary Before Removing Content--")
    print(f"Dictionary Before Removing Content: {dict}")

    print(f"--Deleting Key Value Pair in Dictionary--")
    print(f"Dictionary Contains Content: {dict}")
    key_to_delete = key_list[0]
    print(f"Querying the Dictionary for: {key_to_delete}...")
    print(f"Value Found to be Paired with {key_to_delete}: {dict.get(key_to_delete)}")
    print(f"Removing the Key {key_to_delete} from Dictionary...")
    dict.pop(key_to_delete)
    print(f"Querying the Dictionary for: {key_to_delete}...")
    print(f"Value Found to be Paired with {key_to_delete}: {dict.get(key_to_delete)}")

    print(f"--Displaying to Dictionary After Removing Content--")
    print(f"Dictionary After Removing Content: {dict}")

    """
    When a key is removed in Hash Tables, the memory associated with the key value pair
    is given a flag saying that it has been removed. The memory itself usually still exists
    in the Hash Table, but the ability for the Hash Table to locate it and return it has
    gone away. This memory removed flag is also utilized by the hashing algorithm when
    trying to find the key value pair associated with a key, as the location being marked
    as having data previously removed is important for it to correctly find the key value
    pair it is looking for.
    """

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    print(f"--Displaying to Dictionary Before Removing Content--")
    print(f"Dictionary Before Removing Content: {dict}")

    print(f"--Deleting A Missing Key Value Pair in Dictionary--")
    nonexistent_key = "Jellyfish"
    print(f"Attempting to Remove {nonexistent_key} from Dictionary...")
    try:
        print(f"Popping {nonexistent_key} from Dictionary Returned: {dict.pop(nonexistent_key)}")
    except Exception as e:
        print(f"Popping {nonexistent_key} from Dictionary Threw an Error: {e}")

    print(f"--Displaying to Dictionary After Removing Content--")
    print(f"Dictionary After Removing Content: {dict}")

    """
    In this case, when searching for a key to remove from a Dictionary that does not contain
    the key, the Dictionary will throw an error. This is because the outcome of removing a
    non existent key is meaningfully different than removing a key due to the fact that Python
    returns the value associated with the key when removing. If there is no key associated
    with a value, the return of None will be the same as the return of removing the key when
    it has the value of None associated with it.
    """

    print(f"--Using Empty Dictionary--")

    print(f"--Creating New Dictionary--")
    dict_empty = {}
    print(f"Dictionary Created with Content: {dict_empty}")
    key_empty = "Walrus"
    print(f"Querying the Dictionary for: {key_empty}...")
    print(f"Value Found to be Paired with {key_empty}: {dict_empty.get(key_empty)}")

    print(f"--Displaying to Dictionary After Query--")
    print(f"Dictionary After Query: {dict_empty}")

    """
    Empty Dictionaries work in the same way as a Dictionary with data. When they
    are queried for key value pairs, the return of None will be given for every
    key because they do not contain the key value pair.
    """

    # ========================================
    # REAL WORLD SCENARIO: DAILY CHORE LIST
    # ========================================

    print("\n=== REAL WORLD SCENARIO: DAILY CHORE LIST ===")

    print(f"--Creating Daily Chores List--")
    chore_list = {}
    chores = ["Clean Dishes", "Wash Clothes", "Get Groceries", "Walk Dog", "Clip Hedges"]
    status = [False, False, True, False, False]
    for i in range(len(chores)):
        print(f"Chore to Chore List: {chores[i]}:{status[i]}")
        chore_list.update({chores[i]: status[i]})
    print(f"Current Chore List: {chore_list}")

    print(f"--Assess Chores--")
    for chore, status in chore_list.items():
        if not status:
            print(f"Taking Care of Chore: {chore}...")
            chore_list.update({chore: not status})
            print(f"Chore Done!")
            print(f"Current Chore List: {chore_list}")
    print(f"Nice Work, All Chores Complete!")


if __name__ == "__main__":
    main()