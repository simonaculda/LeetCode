import unittest
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.
"""


def findMin(nums):
    """

    :param nums: List[int]
    :return: int
    """
    # left = 0
    # right = len(nums) - 1
    # while left < right:
    #     middle = (left + right) // 2
    #     if nums[left] > nums[middle]:
    #         if nums[middle -1] < nums[middle]:
    #             right = middle
    #         else:
    #             return nums[middle]
    #     else:
    #         if nums[middle -1] > nums[middle]:
    #             return nums[middle]
    #         elif nums[right] > nums[middle]:
    #             right = middle
    #         else:
    #             left = middle + 1
    # return min(nums[left], nums[right])

    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    return nums[left]


# print(findMin([4, 5, 6, 7, 0, 1, 2]))
# print(findMin([4,5,6,7,0,1,2]))
# print(findMin([3,4,5,1,2] ))
# print(findMin([1, 2,3 ,4]))
# print(findMin([5, 1, 2, 3, 4]))
# print(findMin([1]))
# print(findMin([]))


class Test(unittest.TestCase):
    def test(self, sol):
        self.assertEqual(sol([4, 5, 6, 7, 0, 1, 2]), 0)


if __name__ == "__main__":
    # unittest.main()
    t = Test()
    t.test(findMin)