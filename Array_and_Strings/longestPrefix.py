"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


def longestCommonPrefix( strs):
    """
    :param strs: List[str]
    :return: str
    """
    if len(strs) == 0:
        return ""
    else:
        it = 0
    for it in range(len(strs[0])):
        for i in range(0, len(strs)):
            if it >= len(strs[i]) or strs[0][it] != strs[i][it]:
                return strs[0][:it]

    if it >= 0:
        return strs[0][:it+1]
    else:
        return ""


words = ["flower", "flow", "flight"]
print(longestCommonPrefix(["aa", "a"]))
