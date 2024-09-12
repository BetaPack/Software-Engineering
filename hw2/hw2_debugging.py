"""
Merge Sort Implementation

In this module we implement the merge sort algorithm.
The module includes two main functions:

1. merge_sort: Splits and sorts a provided array of elements recursively.
2. recombine: Merges two sorted lists into a single sorted list.
"""

import logging
import rand

# Set up logging configuration
logging.basicConfig(
    filename="debugging.log",
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
    )
logging.debug("CORRECT LOG")
logger = logging.getLogger("Debugging HW2")

unsorted_arr = rand.random_array([None] * 20)
logger.debug("Generated random array: %s", unsorted_arr)

if any(x is None for x in unsorted_arr):
    logger.error("Array contains None values after generation! Check random_array function.")
else:
    logger.debug("Array correctly generated with no None values.")

def merge_sort(arr):
    """
    Performs the merge sort on arr.

    Parameters:
    arr: The list of elements to be sorted.

    Returns:
    list: A new list containing all the elements from `arr`,
    in a sorted order
    """
    logging.debug("Starting merge_sort on array: %s", arr)

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    left_sorted = merge_sort(arr[:half])
    logging.debug("Left half sorted: %s", left_sorted)

    right_sorted = merge_sort(arr[half:])
    logging.debug("Right half sorted: %s", right_sorted)
    return recombine(left_sorted, right_sorted)

def recombine(left_arr, right_arr):
    """
    Function to merge two sorted lists into a single sorted list.

    Parameters:
    left_arr (list): The first sorted list.
    right_arr (list): The second sorted list.

    Returns:
    list: A merged and sorted list containing all elements from `left_arr` 
    and `right_arr`.
    """

    logger.debug("Recombining arrays: Left = %s, Right = %s", left_arr, right_arr)
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] is None or right_arr[right_index] is None:
            logger.error(
                "None value encountered in recombine! Left: %s, Right: %s",
                 left_arr[left_index], right_arr[right_index])
            return merge_arr

        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    logger.debug("Merged array: %s", merge_arr)
    return merge_arr

arr_out = merge_sort(unsorted_arr)
logger.debug("Final sorted array: %s", arr_out)

print(arr_out)
