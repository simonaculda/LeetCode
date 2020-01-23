"""
    Given an array, rotate the array to the right by k steps, where k is non-negative.
    Example :

    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rotate(nums, k):
    """

    :param nums: List[int]
    :param k: int
    :return: Do not modify anything, do the operations inplace
    """
    if k > len(nums):
        k = k % len(nums)
    for i in range(k):
        element = nums.pop()
        nums.insert(0, element)
    return nums


print(rotate([1,2,3,4,5,6,7], 3))