"""
    Implement strStr().
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
def strStr(haystack, needle):
    """

    :param haystack: Str
    :param needle: Str
    :return: index: int, index of the first occurrence of needle in haystack
            -1 if needle is not part of haystack
    """
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


print(strStr("", ""))