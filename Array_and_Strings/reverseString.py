"""
    Write a function that reverses a string. The input string is given as an array of characters char[].
    Do not allocate extra space for another array, you must do this by modifying the
    input array in-place with O(1) extra memory.
"""


def reverseString(s):
    """

    :param s: List[strs]
    :return: It does't return nothing, we make the changes in place with O(1) extra memory
    """

    lens = len(s)
    for i in range(lens//2):
        aux = s[i]
        s[i] = s[lens-1-i]
        s[lens-1-i] = aux
    return s
    # s.reverse()

print(reverseString(["h","e","l","l","o"]))
