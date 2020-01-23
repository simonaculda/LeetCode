"""
Given a string and an integer k, you need to reverse the first k characters for
every 2k characters counting from the start of the string. If there are less than k characters left,
reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the
first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""

def reverseStr(s, k):
    """

    :param s: str
    :param k: int
    :return: str
    """
    i = 0
    result = ""
    while i <= len(s):

        result += s[i:i+k][::-1]
        result += s[i+k: i + 2 * k]
        i = i + 2 * k
    return result


print(reverseStr('abcdefg', 2))
print(reverseStr("cam", 3))
l = 'abcd'
print(l[0:2][::-1])