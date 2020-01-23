"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and
only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2
"""
def mySqrt(x):
    """

    :param x: int
    :return: int
    """
    left = 0
    right = x // 2
    while left <= right:
        middle = (left + right) // 2
        # print("left is {} right is {} and middle is {} ".format(left, right, middle))
        if middle ** 2 <= x < (middle + 1) ** 2:
            return middle
        elif middle ** 2 > x:
            right = middle - 1
        elif middle ** 2 < x:
            left = middle + 1

    # return middle


print(mySqrt(4))