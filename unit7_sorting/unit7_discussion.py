"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

import time

def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Copy of list as it seems like the directions want a separate list
    sort_lst = lst.copy()

    # Store length of List so it does not need to be found more than once
    length = len(sort_lst)

    # Flag for keeping track if a swap has taken place for efficiency
    swap = False

    # Iterate through each value in the list
    for i in range(length):
        # Iterate through each value (besides the last) in the list again
        for j in range(length - 1):

            # Check if the current and next value are in incorrect ascending order
            # Swap if they are not
            if sort_lst[j] > sort_lst[j + 1]:
                hold = sort_lst[j]
                sort_lst[j] = sort_lst[j + 1]
                sort_lst[j + 1] = hold

                # Note that a swap was done
                swap = True

        # Break out of loop if list is currently sorted
        if not swap:
            break

        # Reset swap flag for next iteration
        swap = False

    return sort_lst


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Store length of list
    length = len(lst)

    # Return a new list immediately if already sorted
    if length <= 1:
        return lst.copy()

    # Get middle index of list
    mid_index = length // 2

    # Merge sort the lower half of the list
    low_lst = merge_sort(lst[:mid_index])
    # Merge sort the upper half of the list
    high_lst = merge_sort(lst[mid_index:])

    # Merge the lower and upper halves together and return
    return merge(low_lst, high_lst)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    # Create new empty list for sorted values
    lst = []

    # Initialize components for merging logic
    left_index = 0
    left_length = len(left)
    right_index = 0
    right_length = len(right)

    # Flag for knowing if fully merged
    merged = False

    # While not merged, continue merging
    while not merged:
        # Case of left list is already fully merged
        if left_index >= left_length:
            lst.append(right[right_index])
            right_index += 1

        # Case of right list is already fully merged
        elif right_index >= right_length:
            lst.append(left[left_index])
            left_index += 1

        # Case of next left value is less than next right value
        elif left[left_index] < right[right_index]:
            lst.append(left[left_index])
            left_index += 1

        # Case of next right value is less than or equal to next left value
        else:
            lst.append(right[right_index])
            right_index += 1

        # Check if there are still values to merge
        if (left_index >= left_length) and (right_index >= right_length):
            merged = True

    # Return new fully merged and sorted list
    return lst

def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    print(f"--Creating New List for Sorting Algorithms--")
    lst_bubble1 = [40, 33, 102, 7, 8, 90, 22, 61, 68]
    lst_merge1 = lst_bubble1.copy()
    print(f"List to be Sorted by Sorting Algorithms: {lst_bubble1}")

    print(f"--Sorting List with Bubble Sort--")
    print(f"List Before Applying Bubble Sort: {lst_bubble1}")
    start_time_bub1 = time.perf_counter()
    lst_bubble1 = bubble_sort(lst_bubble1)
    end_time_bub1 = time.perf_counter()
    time_dif_bub1 = end_time_bub1 - start_time_bub1
    print(f"List After Applying Bubble Sort: {lst_bubble1}")
    print(f"Bubble Performance: {time_dif_bub1: .8f} seconds")

    print(f"--Sorting List with Merge Sort--")
    print(f"List Before Applying Merge Sort: {lst_merge1}")
    start_time_mer1 = time.perf_counter()
    lst_merge1 = merge_sort(lst_merge1)
    end_time_mer1 = time.perf_counter()
    time_dif_mer1 = end_time_mer1 - start_time_mer1
    print(f"List After Applying Merge Sort: {lst_merge1}")
    print(f"Merge Performance: {time_dif_mer1: .8f} seconds")

    print(f"--Checking Sorted List Outcome--")
    print(f"Bubble Sort Outcome: {lst_bubble1}")
    print(f"Merge Sort Outcome: {lst_merge1}")
    equivalent = True
    for i in range(len(lst_bubble1)):
        if lst_bubble1[i] != lst_merge1[i]:
            equivalent = False
            break
    if equivalent:
        print(f"Outcome from Bubble Sort and Merge Sort are Equivalent!")
    else:
        print(f"Outcome from Bubble Sort and Merge Sort are Different!")
    if time_dif_mer1 > time_dif_bub1:
        print(f"Merge Sort took{((time_dif_mer1 - time_dif_bub1) / time_dif_bub1): .2%} longer!")
    elif time_dif_mer1 < time_dif_bub1:
        print(f"Bubble Sort took{((time_dif_bub1 - time_dif_mer1) / time_dif_mer1): .2%} longer!")
    else:
        print(f"Bubble Sort and Merge Sort took the Same Amount of Time: {time_dif_mer1}")



    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    print(f"--Creating New List for Sorting Algorithms--")
    lst_bubble2 = [-3, 0, 20, 33, 0, -4, 7, 21, 54, 79, 12, 11]
    lst_merge2 = lst_bubble2.copy()
    print(f"List to be Sorted by Sorting Algorithms: {lst_bubble2}")

    print(f"--Sorting List with Bubble Sort--")
    print(f"List Before Applying Bubble Sort: {lst_bubble2}")
    start_time_bub2 = time.perf_counter()
    lst_bubble2 = bubble_sort(lst_bubble2)
    end_time_bub2 = time.perf_counter()
    time_dif_bub2 = end_time_bub2 - start_time_bub2
    print(f"List After Applying Bubble Sort: {lst_bubble2}")
    print(f"Bubble Performance: {time_dif_bub2: .8f} seconds")

    print(f"--Sorting List with Merge Sort--")
    print(f"List Before Applying Merge Sort: {lst_merge2}")
    start_time_mer2 = time.perf_counter()
    lst_merge2 = merge_sort(lst_merge2)
    end_time_mer2 = time.perf_counter()
    time_dif_mer2 = end_time_mer2 - start_time_mer2
    print(f"List After Applying Merge Sort: {lst_merge2}")
    print(f"Merge Performance: {time_dif_mer2: .8f} seconds")

    print(f"--Checking Sorted List Outcome--")
    print(f"Bubble Sort Outcome: {lst_bubble2}")
    print(f"Merge Sort Outcome: {lst_merge2}")
    equivalent = True
    for i in range(len(lst_bubble2)):
        if lst_bubble2[i] != lst_merge2[i]:
            equivalent = False
            break
    if equivalent:
        print(f"Outcome from Bubble Sort and Merge Sort are Equivalent!")
    else:
        print(f"Outcome from Bubble Sort and Merge Sort are Different!")
    if time_dif_mer2 > time_dif_bub2:
        print(f"Merge Sort took{((time_dif_mer2 - time_dif_bub2) / time_dif_bub2): .2%} longer!")
    elif time_dif_mer2 < time_dif_bub2:
        print(f"Bubble Sort took{((time_dif_bub2 - time_dif_mer2) / time_dif_mer2): .2%} longer!")
    else:
        print(f"Bubble Sort and Merge Sort took the Same Amount of Time: {time_dif_mer2}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print(f"--Creating Empty List for Sorting Algorithms--")
    lst_bubble_empty = []
    lst_merge_empty = lst_bubble_empty.copy()
    print(f"List to be Sorted by Sorting Algorithms: {lst_bubble_empty}")

    print(f"--Sorting List with Bubble Sort--")
    print(f"List Before Applying Bubble Sort: {lst_bubble_empty}")
    start_time_bub_empty = time.perf_counter()
    lst_bubble_empty = bubble_sort(lst_bubble_empty)
    end_time_bub_empty = time.perf_counter()
    time_dif_bub_empty = end_time_bub_empty - start_time_bub_empty
    print(f"List After Applying Bubble Sort: {lst_bubble_empty}")
    print(f"Bubble Performance: {time_dif_bub_empty: .8f} seconds")

    print(f"--Sorting List with Merge Sort--")
    print(f"List Before Applying Merge Sort: {lst_merge_empty}")
    start_time_mer_empty = time.perf_counter()
    lst_merge_empty = merge_sort(lst_merge_empty)
    end_time_mer_empty = time.perf_counter()
    time_dif_mer_empty = end_time_mer_empty - start_time_mer_empty
    print(f"List After Applying Merge Sort: {lst_merge_empty}")
    print(f"Merge Performance: {time_dif_mer_empty: .8f} seconds")

    print(f"--Checking Sorted List Outcome--")
    print(f"Bubble Sort Outcome: {lst_bubble_empty}")
    print(f"Merge Sort Outcome: {lst_merge_empty}")
    equivalent = True
    for i in range(len(lst_bubble_empty)):
        if lst_bubble_empty[i] != lst_merge_empty[i]:
            equivalent = False
            break
    if equivalent:
        print(f"Outcome from Bubble Sort and Merge Sort are Equivalent!")
    else:
        print(f"Outcome from Bubble Sort and Merge Sort are Different!")
    if time_dif_mer_empty > time_dif_bub_empty:
        print(f"Merge Sort took{((time_dif_mer_empty - time_dif_bub_empty) / time_dif_bub_empty): .2%} longer!")
    elif time_dif_mer_empty < time_dif_bub_empty:
        print(f"Bubble Sort took{((time_dif_bub_empty - time_dif_mer_empty) / time_dif_mer_empty): .2%} longer!")
    else:
        print(f"Bubble Sort and Merge Sort took the Same Amount of Time: {time_dif_mer_empty}")

    """
    For the empty list edge case, Bubble Sort immediately returns the new empty
    list due to the for loops already being completed and thus not iterated on.
    For Merge sort, the first check of whether the list is empty or contains one
    element is triggered and returns a new empty list copy immediately.
    """

    print(f"\n--Creating Reverse Sorted List for Sorting Algorithms--")
    lst_bubble_reverse = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
    lst_merge_reverse = lst_bubble_reverse.copy()
    print(f"List to be Sorted by Sorting Algorithms: {lst_bubble_reverse}")

    print(f"--Sorting List with Bubble Sort--")
    print(f"List Before Applying Bubble Sort: {lst_bubble_reverse}")
    start_time_bub_reverse = time.perf_counter()
    lst_bubble_reverse = bubble_sort(lst_bubble_reverse)
    end_time_bub_reverse = time.perf_counter()
    time_dif_bub_reverse = end_time_bub_reverse - start_time_bub_reverse
    print(f"List After Applying Bubble Sort: {lst_bubble_reverse}")
    print(f"Bubble Performance: {time_dif_bub_reverse: .8f} seconds")

    print(f"--Sorting List with Merge Sort--")
    print(f"List Before Applying Merge Sort: {lst_merge_reverse}")
    start_time_mer_reverse = time.perf_counter()
    lst_merge_reverse = merge_sort(lst_merge_reverse)
    end_time_mer_reverse = time.perf_counter()
    time_dif_mer_reverse = end_time_mer_reverse - start_time_mer_reverse
    print(f"List After Applying Merge Sort: {lst_merge_reverse}")
    print(f"Merge Performance: {time_dif_mer_reverse: .8f} seconds")

    print(f"--Checking Sorted List Outcome--")
    print(f"Bubble Sort Outcome: {lst_bubble_reverse}")
    print(f"Merge Sort Outcome: {lst_merge_reverse}")
    equivalent = True
    for i in range(len(lst_bubble_reverse)):
        if lst_bubble_reverse[i] != lst_merge_reverse[i]:
            equivalent = False
            break
    if equivalent:
        print(f"Outcome from Bubble Sort and Merge Sort are Equivalent!")
    else:
        print(f"Outcome from Bubble Sort and Merge Sort are Different!")
    if time_dif_mer_reverse > time_dif_bub_reverse:
        print(f"Merge Sort took{((time_dif_mer_reverse - time_dif_bub_reverse) / time_dif_bub_reverse): .2%} longer!")
    elif time_dif_mer_reverse < time_dif_bub_reverse:
        print(f"Bubble Sort took{((time_dif_bub_reverse - time_dif_mer_reverse) / time_dif_mer_reverse): .2%} longer!")
    else:
        print(f"Bubble Sort and Merge Sort took the Same Amount of Time: {time_dif_mer_reverse}")

    """
    For the reverse edge case, Bubble Sort is undergoing its worse case
    while Merge Sort is not. Bubble Sort is undergoing a swap as many times
    as it can for a given set of data when handed a reverse sorted set of
    data. Merge Sort needs a different data set for it to undergo the most
    operations, one that looks more like {0, 4, 2, 6, 1, 5, 3, 7}, as this
    incurs the most comparisons.
    """

    print(f"\n--Creating Very Long List--")
    lst_bubble_long = list(range(10000, 0, -1))
    lst_merge_long = lst_bubble_long.copy()
    print(f"List to be Sorted by Sorting Algorithms: [{lst_bubble_long[0]},... ,{lst_bubble_long[len(lst_bubble_long) - 1]}]")

    print(f"--Sorting List with Bubble Sort--")
    start_time_bub_long = time.perf_counter()
    lst_bubble_long = bubble_sort(lst_bubble_long)
    end_time_bub_long = time.perf_counter()
    time_dif_bub_long = end_time_bub_long - start_time_bub_long
    print(f"Bubble Performance: {time_dif_bub_long: .8f} seconds")

    print(f"--Sorting List with Merge Sort--")
    start_time_mer_long = time.perf_counter()
    lst_merge_long = merge_sort(lst_merge_long)
    end_time_mer_long = time.perf_counter()
    time_dif_mer_long = end_time_mer_long - start_time_mer_long
    print(f"Merge Performance: {time_dif_mer_long: .8f} seconds")

    print(f"--Checking Sorted List Outcome--")
    # Not displaying lists here due to size, just if they are equivalent
    equivalent = True
    for i in range(len(lst_bubble_long)):
        if lst_bubble_long[i] != lst_merge_long[i]:
            equivalent = False
            break
    if equivalent:
        print(f"Outcome from Bubble Sort and Merge Sort are Equivalent!")
    else:
        print(f"Outcome from Bubble Sort and Merge Sort are Different!")
    if time_dif_mer_long > time_dif_bub_long:
        print(f"Merge Sort took{((time_dif_mer_long - time_dif_bub_long) / time_dif_bub_long): .2%} longer!")
    elif time_dif_mer_long < time_dif_bub_long:
        print(f"Bubble Sort took{((time_dif_bub_long - time_dif_mer_long) / time_dif_mer_long): .2%} longer!")
    else:
        print(f"Bubble Sort and Merge Sort took the Same Amount of Time: {time_dif_mer_long}")


    # ========================================
    # REAL WORLD SCENARIO: ALPHABETICAL NAMES
    # ========================================

    print("\n=== REAL WORLD SCENARIO: ALPHABETICAL NAMES ===")

    print(f"--Creating Names List--")
    names_lst = ["Angela", "Rebecca", "Johnathan", "Gregory", "Samuel", "Alex"]
    print(f"Names List That Need to be Sorted: {names_lst}")

    print(f"--Sorting Names List--")
    names_lst = bubble_sort(names_lst)
    print(f"Names List After Sorting Alphabetically: {names_lst}")
    print(f"Names Successfully Sorted!")

    # =====================================
    # REAL WORLD SCENARIO: CONTEST RESULTS
    # =====================================

    print("\n=== REAL WORLD SCENARIO: CONTEST RESULTS ===")

    print(f"--Conducting Contest--")
    print(f"Contest Taking Place, Participants Getting Scores...")
    contest_results = {"Poppy":4, "Sammy":6, "Dmitri":2, "Kyle":3}
    print(f"Results at the End of the Contest: {contest_results}")

    print(f"--Getting Ascending Scores--")
    scores = list(contest_results.values())
    print(f"Scores of Contest: {scores}")
    scores = merge_sort(scores)
    print(f"Scores in Ascending Value: {scores}")

    print(f"--Using Scores to Create Descending Results--")
    contest_results_sorted = {}
    for score in reversed(scores):
        for key in contest_results:
            if contest_results[key] == score:
                contest_results_sorted.update({key: score})
                break
    print(f"Contest Results in Ascending Value: {contest_results_sorted}")
    print(f"Congrats to {next(iter(contest_results_sorted))} on First Place!")


if __name__ == "__main__":
    main()