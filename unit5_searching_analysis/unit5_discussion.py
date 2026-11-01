"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Iterate through each value, returning the index of the first matching value
    for index, value in enumerate(lst):
        if value == target:
            return index

    # Default return of -1
    return -1

    """
        Linear search has O(N) time complexity because the worst case for linear search requires
    the algorithm to check every index in the list once. The algorithm cannot know if the value is or
    is not in the collection unless every value in the collection are checked. This leads to O(N)
    time complexity.
    """


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Return -1 if empty list
    if not lst:
        return -1

    # Initialize low and high boundaries
    low = 0
    high = len(lst) - 1

    # Check for if value can exist in sorted list, return -1 if it cannot
    if lst[low] > target or lst[high] < target:
        return -1

    # Set mid to half of high if high is not equal to 0 to make sure no division by 0
    if high != 0:
        mid = int(high/2)
    else:
        mid = 0

    # Binary Search loop

    # Exit loop when boundaries no longer make sense, indicating value does not exist in collection
    while low <= high:

        # Store mid_value in local variable
        mid_value = lst[mid]

        # Return found index if mid_value is the target
        if mid_value == target:
            return mid

        # Adjust boundaries by either moving low or high
        # Both adjustments shrink the pool of possible indexes by approximately half
        if mid_value < target:
            # Move low above mid if the value is greater than mid
            low = mid + 1
        else:
            # Move high below mid if value is lower than mid
            high = mid -1

        # Set mid to between low and high making sure not to divide by 0
        if high != low:
            mid = int((high - low)/2) + low
        else:
            # Setting mid to low works fine here since low and high are equal
            mid = low

    # If algorithm found no valid value, return -1
    return -1

    """
        Each iteration affects the search space by reducing it by half. Since the list is sorted,
    the algorithm can find information about the rest of the list by knowing the value and index
    for the current value in the middle. If the value in the middle of the remaining indexes
    is below the value being searched for, the lower half remaining indexes are ruled out. If the
    value in the middle of the remaining indexes is above the value being searched for, the upper
    half of the remaining indexes are ruled out. This is what leads to the O(logN) time complexity
    behavior of binary search
    """


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    print(f"--Creating Small Dataset--")
    data_small = [2, 7, 15, 18, 22, 30, 35]
    print(f"Small Dataset Created with Content: {data_small}")

    print(f"--Linear Search for Existing Value--")
    lin_ex_small = 30
    print(f"Result for searching {lin_ex_small} in Linear Search: {linear_search(data_small, lin_ex_small)}")
    # Data is linearly iterated through until the value is found

    print(f"--Linear Search for Non Existing Value--")
    lin_non_small = 1
    print(f"Result for searching {lin_non_small} in Linear Search: {linear_search(data_small, lin_non_small)}")
    # Data is linearly iterated through until no data is left, and -1 is returned

    print(f"--Binary Search for Existing Value--")
    bin_ex_small = 15
    print(f"Result for searching {bin_ex_small} in Binary Search: {binary_search(data_small, bin_ex_small)}")
    # Data search space is halved with each iteration until the value is found

    print(f"--Binary Search for Non Existing Value--")
    bin_non_small = 8
    print(f"Result for searching {bin_non_small} in Binary Search: {binary_search(data_small, bin_non_small)}")
    # Data search space is halved with each iteration until no data space remains, and -1 is returned

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    print(f"--Creating Very Large Dataset--")
    min_value = 1
    max_value = 499_999_999
    step = 2
    data_large = list(range(min_value, max_value, step))
    print(f"Large Dataset Created with Content: [{min_value}, ... , {max_value}], Length: {len(data_large)}")

    print(f"--Linear Search for Existing Value--")
    lin_ex_large = 20_001
    print(f"Result for searching {lin_ex_large} in Linear Search: {linear_search(data_large, lin_ex_large)}")

    print(f"--Linear Search for Non Existing Value--")
    start_time_lin = time.perf_counter()
    lin_non_large = 30_000
    print(f"Result for searching {lin_non_large} in Linear Search: {linear_search(data_large, lin_non_large)}")
    end_time_lin = time.perf_counter()
    time_dif_lin = end_time_lin - start_time_lin
    print(f"Worst Case Linear Performance: {time_dif_lin: .8f} seconds")

    print(f"--Binary Search for Existing Value--")
    bin_ex_large = 10_001
    print(f"Result for searching {bin_ex_large} in Binary Search: {binary_search(data_large, bin_ex_large)}")

    print(f"--Binary Search for Non Existing Value--")
    start_time_bin = time.perf_counter()
    bin_non_large = 5_000
    print(f"Result for searching {bin_non_large} in Binary Search: {binary_search(data_large, bin_non_large)}")
    end_time_bin = time.perf_counter()
    time_dif_bin = end_time_bin - start_time_bin
    print(f"Worst Case Binary Performance: {time_dif_bin: .8f} seconds")

    print(f"--Worst Case Processing Difference--")
    time_dif_alg = time_dif_lin - time_dif_bin
    print(f"Worst Case Linear Performance - Binary Performance: {time_dif_alg: .8f} seconds")
    print(f"Linear Takes {time_dif_lin/time_dif_bin: .2f} Times Longer than Binary")


    """
        Binary search becomes significantly more efficient compared to linear search as data sets
    grow in size due to their time complexity. Binary search has a time complexity of O(logN) while
    linear search has time complexity of O(N). This relationship causes very large datasets to be
    interpreted in significantly less time and processing power with binary search than linear search.
    """

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print(f"--Creating Empty Dataset--")
    data_empty = []
    print(f"Empty Dataset Created with Content: {data_empty}")

    print(f"--Linear Search for Value in Empty List--")
    lin_empty = 55
    print(f"Result for searching {lin_empty} in Linear Search: {linear_search(data_empty, lin_empty)}")
    # Linear search for loop does not iterate as there is no values to search through, returning the default value

    print(f"--Binary Search for Value in Empty List--")
    bin_empty = 45
    print(f"Result for searching {bin_empty} in Linear Search: {binary_search(data_empty, bin_empty)}")
    # Binary search checks whether the list is empty before searching, and since it is, returns the default value


    print(f"--Creating Single Value Dataset--")
    data_single_ex = [12]
    print(f"Dataset with One Value Created with Content: {data_single_ex}")

    print(f"--Linear Search for Value in Single Value List--")
    lin_single_ex = 12
    print(f"Result for searching {lin_single_ex} in Linear Search: {linear_search(data_single_ex, lin_single_ex)}")
    # Searches for value using only value in list, finds it, returns index 0

    print(f"--Linear Search for Non Existent Value in Single Value List--")
    lin_single_non = 13
    print(f"Result for searching {lin_single_non} in Linear Search: {linear_search(data_single_ex, lin_single_non)}")
    # Searches for value using only value in list, does not find it, returns index -1

    print(f"--Binary Search for Value in Single Value List--")
    bin_single_ex = 12
    print(f"Result for searching {bin_single_ex} in Linear Search: {binary_search(data_single_ex, bin_single_ex)}")
    # Starts search with middle immediately on the single value, recognized middle is the value, returns middle index

    print(f"--Binary Search for Non Existent Value in Single Value List--")
    bin_single_non = 13
    print(f"Result for searching {bin_single_non} in Linear Search: {binary_search(data_single_ex, bin_single_non)}")
    # Goes through one iteration of the binary search algorithm and the range is already invalid, returns default -1

    # ===============================================
    # REAL WORLD SCENARIO: BOOK WITH MISSING PAGES
    # ===============================================

    print("\n=== REAL WORLD SCENARIO: BOOK WITH MISSING PAGES ===")

    print(f"--Creating Book with Missing Pages--")
    book = [1, 2, 5, 6, 7, 9, 10, 11, 17, 18, 19, 20]
    print(f"Book with Missing Pages Created: [{book[0]}, ... , {book[len(book) - 1]}]")

    print(f"--Linearly Checking if Book Contains Page--")
    page_lin = 16
    print(f"Searching for Page {page_lin} in book...")
    if linear_search(book, page_lin) == -1:
        print(f"Could not find Page {page_lin} in book.")
    else:
        print(f"Found Page {page_lin} in book!")

    print(f"--Binarily Checking if Book Contains Page--")
    page_bin = 11
    print(f"Searching for Page {page_bin} in book...")
    if binary_search(book, page_bin) == -1:
        print(f"Could not find Page {page_bin} in book.")
    else:
        print(f"Found Page {page_bin} in book!")

if __name__ == "__main__":
    main()