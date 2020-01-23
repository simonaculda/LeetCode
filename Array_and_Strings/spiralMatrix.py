"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
https://leetcode.com/problems/spiral-matrix/
Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""


def spiralOrder(matrix):
    """

    :param matrix: List[List[int]]
    :return: List[int]
    """
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    result = []
    if min(m, n) % 2 == 0:
        endF = min(m, n)//2
    else:
        endF = min(m, n) // 2 + 1
    for level in range(0, endF):
        for i in range(level, n-level):
            result.append(matrix[level][i])

        for i in range(level + 1, m - level):
            result.append(matrix[i][n - level - 1])

        for i in range(n - level - 2, level - 1, -1):
            if m - level - 1 != level:
                result.append(matrix[m - level - 1][i])

        for i in range(m - level - 2, level, -1):
            if min(m, n)//2 > 0 and level != n - level - 1:
                result.append(matrix[i][level])

    return result


def test():
    assert spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [16, 15, 14]]) == [1, 2, 3, 6, 9, 14, 15, 16, 7, 4, 5, 8]
    assert spiralOrder([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]) ==\
           [2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12]
    assert spiralOrder([]) == []
    assert spiralOrder([[1, 2, 3, 4, 13], [5, 6, 7, 8, 14], [9, 10, 11, 12, 15]]) == \
           [1, 2, 3, 4, 13, 14, 15, 12, 11, 10, 9, 5, 6, 7, 8]
    assert spiralOrder([[1]]) == [1]
    assert spiralOrder([[3], [4], [5]]) == [3, 4, 5]
    assert spiralOrder([[2, 5, 8], [4, 0, 2]]) == [2, 5, 8, 2, 0, 4]


if __name__ == '__main__':
    test()
