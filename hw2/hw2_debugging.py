import logging
import rand

# Set up logging configuration
logging.basicConfig(filename="debugging.log", encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("CORRECT LOG")
logger = logging.getLogger("Debugging HW2")

arr = rand.random_array([None] * 20)
logger.debug(f"Generated random array: {arr}")

if any(x is None for x in arr):
    logger.error("Array contains None values after generation! Check random_array function.")
else:
    logger.debug("Array correctly generated with no None values.")

def mergeSort(arr):
    logging.debug(f"Starting mergeSort on array: {arr}")

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    leftSorted = mergeSort(arr[:half])
    logging.debug(f"Left half sorted: {leftSorted}")

    rightSorted = mergeSort(arr[half:])
    logging.debug(f"Right half sorted: {rightSorted}")
    
    return recombine(leftSorted, rightSorted)

def recombine(leftArr, rightArr):
    logger.debug(f"Recombining arrays: Left = {leftArr}, Right = {rightArr}")
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] is None or rightArr[rightIndex] is None:
            logger.error(f"None value encountered in recombine! Left: {leftArr[leftIndex]}, Right: {rightArr[rightIndex]}")
            return mergeArr

        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    while leftIndex < len(leftArr):
        mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        leftIndex += 1

    while rightIndex < len(rightArr):
        mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        rightIndex += 1

    logger.debug(f"Merged array: {mergeArr}")
    return mergeArr

arr_out = mergeSort(arr)
logger.debug(f"Final sorted array: {arr_out}")

print(arr_out)
