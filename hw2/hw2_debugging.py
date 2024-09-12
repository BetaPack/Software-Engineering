import logging
import rand
import os

# Set up logging configuration
logging.basicConfig(filename=os.path.join(os.getcwd(), 'hw2/logs/hw2_debugging.log'), encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logger = logging.getLogger("Debugging HW2")

def mergeSort(arr):
    logger.debug(f"Sorting array: {arr}")
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    # Recursively split and merge
    left = mergeSort(arr[:half])
    right = mergeSort(arr[half:])
    
    return recombine(left, right)

def recombine(leftArr, rightArr):
    logger.debug(f"Recombining: {leftArr}, {rightArr}")
    
    leftIndex = 0
    rightIndex = 0
    mergeArr = []

    # Merge the two arrays
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] <= rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    # If there are remaining elements in leftArr, add them
    while leftIndex < len(leftArr):
        mergeArr.append(leftArr[leftIndex])
        leftIndex += 1

    # If there are remaining elements in rightArr, add them
    while rightIndex < len(rightArr):
        mergeArr.append(rightArr[rightIndex])
        rightIndex += 1

    logger.debug(f"Merged array: {mergeArr}")
    return mergeArr

# Generate random array using the rand library
arr = rand.random_array([None] * 20)
logger.debug(f"Initial array: {arr}")

# Call mergeSort correctly
arr_out = mergeSort(arr)
logger.debug(f"Sorted array: {arr_out}")

print(arr_out)
