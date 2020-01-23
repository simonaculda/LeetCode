"""
    In a given integer array nums, there is always exactly one largest element.
    Find whether the largest element in the array is at least twice as much as every other number in the array.
    If it is, return the index of the largest element, otherwise return -1.
"""

def dominantIndex( nums):
    """

    :param nums: List[int]
    :return: int - index of te largest elent
                 -1 otherwise
    """
    if len(nums)> 1:
        max_list = max(nums)
        index_max = nums.index(max_list)
        nums.pop(index_max)
        new_max = max(nums)
        if new_max * 2 <= max_list:
            return index_max
        else:
            return -1
    else:
        return 0



print(dominantIndex([3, 6, 1, 0]))
print(dominantIndex([1, 2, 3, 4]))
print(dominantIndex([1]))