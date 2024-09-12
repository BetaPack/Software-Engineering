from hw2_debugging import mergeSort
import rand

def test_edge_cases_array():
    "Testing the mergeSort function by providing an empty array"
    empty_arr = []
    result1 = mergeSort(empty_arr)

    single_element_arr = [5]
    result2 = mergeSort(single_element_arr)

    error_string = ""

    if(result1 == empty_arr and result2 == single_element_arr):
        print("Test Case: 'Edge Cases' - Passed !!!")
        return
    if(result1 != empty_arr):
        error_string = error_string + "Test Case: 'Empty Array' - Failed !!!\n"
    if(result2 != single_element_arr):
        error_string = error_string + "Test Case: 'Single Element Array' - Failed !!!\n"

    assert False, error_string

def test_unsorted_array():
    """
    Testing the mergeSort function by providing an random unsorted array
    """
    unsorted_arr = rand.random_array([None] * 20)
    result = mergeSort(unsorted_arr)  
    sorted_arr = unsorted_arr.copy()
    sorted_arr.sort()

    assert result==sorted_arr, f"Test Case: 'Unsorted Array' - Failed !!!"
    print("Test Case: 'Unsorted Array' - Passed !!!")
    return

def test_sorted_array():
    unsorted_arr = rand.random_array([None] * 20)
    sorted_arr = unsorted_arr.copy()
    sorted_arr.sort()
    reverse_sorted_arr = sorted_arr[::-1]

    result1 = mergeSort(sorted_arr)
    result2 = mergeSort(reverse_sorted_arr)

    error_string = ""

    if(result1 == sorted_arr and result2 == sorted_arr):
        print("Test Case: 'Sorted Array and Reverse Sorted Array' - Passed !!!")
        return
    if(result1 != sorted_arr):
        error_string = error_string + "Test Case: 'Sorted Array' - Failed !!!\n"
    if(result2 != sorted_arr):
        error_string = error_string + "Test Case: 'Reverse Sorted Array' - Failed !!!\n"

    assert False, error_string

if __name__ == "__main__":
    
    try:
        test_edge_cases_array()
    except AssertionError as e:
        print(e)

    try:
        test_unsorted_array()
    except AssertionError as e:
        print(e)

    try:
        test_sorted_array()
    except AssertionError as e:
        print(e)
