"""
    Given a string, you need to reverse the order of characters in each word within a sentence while
    still preserving whitespace and initial word order.

    Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    Note: In the string, each word is separated by single space and there will not be any extra space in the string.
    https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


def reverseWords(s):
    """

    :param s: str
    :return: str
    """
    list_words = s.split()
    for i in range(len(list_words)):
        list_words[i] = list_words[i][::-1]

    return ' '.join(list_words)


def test():
    assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverseWords("Hello word") == "olleH drow"
    assert reverseWords("") == ""
    assert reverseWords("Hi") == "iH"


if __name__ == '__main__':
    test()
