"""
    Given an array of integers that is already sorted in ascending order,
    find two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target,
    where index1 must be less than index2.
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


def twoSum(numbers, target):
    """
    :param numbers: List[int]
    :param target: int
    :return: int, int -  indices of the two numbers such that they add up to the target
    """
    # done = []
    # for i in range(0, len(numbers)-1):
    #     if numbers[i] not in done:
    #         done.append(numbers[i])
    #         for j in range(i + 1, len(numbers)):
    #             if numbers[i] + numbers[j] == target:
    #                 return i+1, j+1
    #             elif numbers[i] + numbers[j] > target:
    #                 break

    left = 0
    right = len(numbers)-1
    while left < right:
        sumn = numbers[left] + numbers[right]
        if sumn == target:
            return left + 1, right + 1
        elif sumn < target:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    assert twoSum([2, 7, 11, 15], 9) == (1, 2)
    assert twoSum([0, 0, 2], 0) == (1, 2)
