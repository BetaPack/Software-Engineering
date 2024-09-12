"""
Random Array Generation in range [1,20]

Functions:
- random_array: Replaces every element in a given list with a random
  integer in range [1,20]

"""

import subprocess


def random_array(arr):
    """
    Generate a list of random integers in the provided array
    in the range[1,20]

    Parameters:
    arr (list): The list to be filled with random integers.

    Returns:
    list: A list filled with random integers between 1 and 20.
    """

    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"],
            capture_output=True,
            check=True
        )
        arr[i] = int(shuffled_num.stdout)
    return arr
