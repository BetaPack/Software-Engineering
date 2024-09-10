import logging

# Set up logging configuration
logging.basicConfig(filename='debugging.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("NEW LOG")

def mergeSort(arr):
    logging.debug(f'Starting mergeSort on array: {arr}')
    
    if len(arr) == 1:
        logging.debug(f'Base case reached with array: {arr}')
        return arr

    half = len(arr) // 2
    logging.debug(f'Splitting array into two halves: {arr[:half]} and {arr[half:]}')
    
    # Recursive call to sort each half
    leftSorted = mergeSort(arr[:half])
    rightSorted = mergeSort(arr[half:])
    
    # Recombine the sorted halves
    return recombine(leftSorted, rightSorted)

def recombine(leftArr, rightArr):
    logging.debug(f'Recombining left: {leftArr} and right: {rightArr}')
    
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1
        logging.debug(f'Updated mergeArr: {mergeArr}')

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + i] = rightArr[i]
        logging.debug(f'Appending remaining elements from rightArr: {mergeArr}')

    for i in range(leftIndex, len(leftArr)):
        mergeArr[i + rightIndex] = leftArr[i]
        logging.debug(f'Appending remaining elements from leftArr: {mergeArr}')

    logging.debug(f'Finished recombining to: {mergeArr}')
    return mergeArr

# Test array
arr = [21, 10, 2, 100, 76, 3, 0, 19, 11, 7]
logging.info(f'Initial array: {arr}')
arr_out = mergeSort(arr)
logging.info(f'Sorted array: {arr_out}')
