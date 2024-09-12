import subprocess

"""
This module provides functionality to generate random arrays using external shuffling provided by shuf command.
"""

def random_array(arr):
    """
    Fills the input list with random integers from 1 to 20 using shuf command.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The list filled with random integers.
    """
    for index, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[index] = int(shuffled_num.stdout)
    return arr
