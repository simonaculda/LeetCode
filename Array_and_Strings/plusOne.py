from functools import reduce
"""
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
def plusOne(digits):
    """
    :param digits: List[int]
    :return: List[int]
    """
    number = reduce(lambda x, y: x * 10 + y, digits)
    number += 1
    return [int(n) for n in str(number)]



print(plusOne([0]))