import math
"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
https://leetcode.com/problems/find-peak-element/
"""


def findPeakElement(nums):
    """

    :param nums: List[int]
    :return: int
    """
    # right = len(nums)
    # nums.insert(0, -math.inf)
    # nums.append(-math.inf)
    # left = 1
    # while left < right:
    #     middle = (left + right) // 2
    #
    #     if nums[middle - 1] < nums[middle] > nums[middle + 1]:
    #         return middle -1
    #     if nums[middle - 1] > nums[middle]:
    #         right = middle
    #     elif nums[middle + 1] > nums[middle]:
    #         left = middle + 1
    #
    # if left <= len(nums) - 1 and nums[left + 1] < nums[left] > nums[left - 1]:
    #     return left -1


    # left = 0
    # right = len(nums) -1
    # while left<right:
    #     mid = (left+right)//2
    #     if nums[mid]>nums[mid+1]:
    #         right = mid
    #     else:
    #         left = mid +1
    # return left

    left, right = 0, len(nums)-1
    while left + 1 < right:
        mid = (left+right) // 2
        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid-1] > nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid
    return left if nums[left] > nums[right] else right


def test():
    assert(findPeakElement([1, 2, 3, 1])) == 2
    assert (findPeakElement([1,2,1,3,5,6,4])) == 5
    assert (findPeakElement([1,2,1,2,3,1])) == 4


if __name__ == "__main__":
    test()
