"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function
to search target in nums. If target exists, then return its index, otherwise return -1.
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


class Solutin(object):
    def search(self, nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: int - index of target in nums
        """
        left = 0
        right = len(nums) -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1


el = Solutin()
print(el.search([-1,0,3,5,9,12], 12))
# print(el.search([-1,0,3,5,9,12], 3))
# l = [1, 2, 3, 4]
# print(l[: 2])
