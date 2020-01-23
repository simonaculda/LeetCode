"""
Given a binary array, find the maximum number of consecutive 1s in this array.
https://leetcode.com/problems/max-consecutive-ones/
"""


def findMaxConsecutiveOnes(nums):
    """

    :param nums: List[int]
    :return: int
    """
    """
    consecutive_one = 0
        result = 0
        for nr in nums:
            if nr == 1:
                consecutive_one +=1
            else:
                result = max(result,consecutive_one)
                consecutive_one = 0
        return max(result,consecutive_one)
    """
    i = 0
    length = 0
    while i < len(nums):
        if nums[i] == 1:
            k = i + 1
            while k < len(nums) and nums[k] == 1:
                k += 1
            if k - i > length:
                length = k - i
            i = k
        elif len(nums) - i > length:
            i += 1
        else:
            break
    return length


def test():
    assert findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert findMaxConsecutiveOnes([0, 0, 0]) == 0
    assert findMaxConsecutiveOnes([]) == 0


if __name__ == '__main__':
    test()

