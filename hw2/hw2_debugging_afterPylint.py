"""
This module provides an implementation of the merge sort algorithm.
It includes detailed logging for debugging purposes.
"""

import logging
import random

# Setup logging configuration
logging.basicConfig(filename='hw2_debugging.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logger = logging.getLogger("Debugging HW2")

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Args:
        arr (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    """
    logger.debug("Sorting array: %s", arr)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return recombine(left, right)

def recombine(left_arr, right_arr):
    """
    Recombines two sorted sublists into one sorted list.
    
    Args:
        left_arr (list): Left half of the split array.
        right_arr (list): Right half of the split array.
    
    Returns:
        list: Merged and sorted list.
    """
    logger.debug("Recombining: %s, %s", left_arr, right_arr)
    
    left_index = 0
    right_index = 0
    merged_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    merged_arr.extend(left_arr[left_index:])
    merged_arr.extend(right_arr[right_index:])

    logger.debug("Merged array: %s", merged_arr)
    return merged_arr

# Generate a random array for testing
array = [random.randint(1, 100) for _ in range(20)]
logger.debug("Initial array: %s", array)
sorted_array = merge_sort(array)
logger.debug("Sorted array: %s", sorted_array)

print(sorted_array)
