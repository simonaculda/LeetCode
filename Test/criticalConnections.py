def criticalConnections(n, connections):
    """

    :param n: int
    :param connections: List[List[int]]
    :return: List[List[int]]
    """
    result = []
    l = []
    for i in range(len(connections)):
        for j in range(0, 2):
            l.append(connections[i][j])

    for j in range(len(l)):
        if l.count(l[j]) == 1:
            result.append(connections[j//2])

    return result


print(criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
print(criticalConnections(6,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
