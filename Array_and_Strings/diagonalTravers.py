"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as
shown in the below example.
https://leetcode.com/problems/diagonal-traverse/
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
"""


def findDiagonalOrder(matrix):
    """

    :param matrix: List[List[int]]
    :return: List[int]
    """
    if not matrix:
        return []
    i, j = 0, 0
    m = len(matrix)-1
    n = len(matrix[0])-1
    result = [matrix[0][0]]
    while i != m or j != n:
        if i == 0 or j == n:
            if i == 0 and j < n:
                j += 1
            elif j == n:
                i += 1
            result.append(matrix[i][j])
            while j != 0 and i < m:
                i += 1
                j -= 1
                result.append(matrix[i][j])
        elif j == 0 or i == m:
            if j == 0 and i < m:
                i += 1
            elif i == m:
                j += 1
            result.append(matrix[i][j])
            while i != 0 and j < n:
                j += 1
                i -= 1
                result.append(matrix[i][j])
    return result


def test():
    assert findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert findDiagonalOrder([[1]]) == [1]
    assert findDiagonalOrder([]) == []


if __name__ == '__main__':
    test()
