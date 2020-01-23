"""
    Given an array of integers nums, write a method that returns the "pivot" index of this array.
"""


def pivot_index(nums):
    """

    :param nums: List[int]
    :return: int - index where the sum of the numbers to the left of the index
    is equal to the sum of the numbers to the right of the index.
            -1 - if we don't find any index like this
    """

    # totalSum = sum(nums)
    # if len(nums) == 0 :
    #     return -1
    # if len(nums) == 1:
    #     return 0
    # for i in range(len(nums)):
    #     if i == 0:
    #         lefSum = 0
    #         rightSum = totalSum - nums[0]
    #     else:
    #         rightSum = rightSum - nums[i]
    #         lefSum = lefSum + nums[i-1]
    #     if lefSum == rightSum:
    #         return i
    # return -1
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        else:
            left_sum += nums[i]
    return -1






print(pivot_index([1, 7, 3, 6, 5, 6]))
