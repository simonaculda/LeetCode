"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
"""


def arrayPairSum(nums):
    """
    :param nums: List[int]
    :return: int
    """
    # sumn = 0
    # nums.sort()
    # for i in range(0,len(nums),2):
    #     sumn += min(nums[i], nums[i+1])
    # return sumn
    nums.sort()
    return sum(nums[0::2])
ar = [1, 4, 3, 2]
print(sum(ar[0::2]))
print(arrayPairSum([1,4,3,2]))