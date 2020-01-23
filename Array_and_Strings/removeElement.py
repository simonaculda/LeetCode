import unittest
"""
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place
    with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeElement(self, nums, val):

        index = 0
        length = len(nums)

        while index < length:
            if nums[index] == val:
                nums.pop(index)
                length -= 1
            else:
                index += 1
        return length


class TestC(unittest.TestCase):

    def testOne(self):
        nums = [3, 2, 2, 3]
        val = 3
        s = Solution()
        result = s.removeElement(nums, val)
        self.assertEquals(result, 2)
        self.assertEquals(s.removeElement([3, 3, 4, 4, 5, 7], 3), 4)


if __name__ == '__main__':

    unittest.main()

