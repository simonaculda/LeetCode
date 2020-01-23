"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
subarray of which the sum ≥ s. If there isn't one, return 0 instead.
"""
def minSubArrayLen(s, nums):
    """

    :param s: int
    :param nums: List[int]
    :return: int
    """
    # lenN = len(nums)
    # sumN = [0] * lenN
    # len_min = 1
    # while len_min <= lenN:
    #     for i in range(lenN - len_min + 1):
    #         sumN[i] = sumN[i] + nums[i + len_min-1]
    #
    #         if sumN[i] >= s:
    #             return len_min
    #     print(sumN)
    #     len_min += 1
    # return 0
    if len(nums) == 0: return 0
    start = end = 0
    sumn  = nums[0]
    el = float('inf')
    while start <= end < len(nums):
        if sumn >= s:
            el = min(el, end-start+1)
            sumn -= nums[start]
            start += 1
        else:
            end += 1
            if end < len(nums):
                sumn += nums[end]
        # print(sumn)
    if el == float('inf'):
        el = 0
    return el


print(minSubArrayLen(7, [2,3,1,2,4,3]))
# print(minSubArrayLen(15, [1, 2, 3, 4, 5]))
# print(minSubArrayLen(100, []))