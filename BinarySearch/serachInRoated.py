"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


def search(nums, target):
    """

    :param nums: List[int]
    :param target: int
    :return: int
    """
    left = 0
    right = len(nums) - 1
    piv = 0
    while nums[right] < nums[piv]:
        piv +=1
        nums.insert(0, nums[right])
        nums.pop()

    # print(piv)
    while left <= right:
        middle = (left + right) // 2
        # print(left, right)
        if nums[middle] == target:
            # print(middle, piv)
            if middle >= piv:
                # print(middle, piv)
                return middle - piv
            elif middle < piv:
                return len(nums) - piv + middle
        if nums[middle] < target:
            left = middle + 1
        if nums[middle] > target:
            right = middle - 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 5))
print(search([1, 2, 3, 4, 5], 5))
print(search([5, 4, 3, 2, 1], 5))
