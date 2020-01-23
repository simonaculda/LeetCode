import unittest
"""
Given an array of integers (positive and negative) find the largest continuous sum.
"""


def large_count_sum(arr):
    if len(arr) == 0:
        return 0

    current_sum = arr[0]
    max_sum = arr[0]
    for nr in arr[1:len(arr)]:
        current_sum = max(current_sum + nr, nr)
        if current_sum > max_sum:  # max_sum = max(current_sum, max_sum)
            max_sum = current_sum

    return max_sum


# class LargeContTest(unittest.TestCase):
#     def test(self, sol):
#         self.assertEqual(sol([1,2,-1,3,4,10,10,-10,-1]), 29)
#         self.assertEqual(sol([0, -1, 1, -3, -5]), 1)
#         self.assertEqual(sol([1,2,-1,3,4,-1]), 9)



class LargestSum(unittest.TestCase):
    def test(self, sol):
        self.assertEqual(sol([1,2,-1,3,4,10,10,-10,-1]), 29)



t = LargestSum()
t.test(large_count_sum)