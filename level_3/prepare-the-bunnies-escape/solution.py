import sys


# User defined Pair class
class Pair:
    def __init__(self, x, y):
        self.first = x
        self.second = y


# Check if it is possible to go to (x, y) from the current
# position. The function returns false if the cell has
# value 0 or already visited
def isSafe(mat, visited, x, y):
    return (
        x >= 0
        and x < len(mat)
        and y >= 0
        and y < len(mat[0])
        # and mat[x][y] == 0
        and (not visited[x][y])
    )


def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):
    if i == x and j == y:
        min_dist = min(dist, min_dist)
        return min_dist

    # set (i, j) cell as visited
    visited[i][j] = True

    # go to the bottom cell
    if isSafe(mat, visited, i + 1, j):
        min_dist = findShortestPath(mat, visited, i + 1, j, x, y, min_dist, dist + 1)

    # go to the right cell
    if isSafe(mat, visited, i, j + 1):
        min_dist = findShortestPath(mat, visited, i, j + 1, x, y, min_dist, dist + 1)

    # go to the top cell
    if isSafe(mat, visited, i - 1, j):
        min_dist = findShortestPath(mat, visited, i - 1, j, x, y, min_dist, dist + 1)

    # go to the left cell
    if isSafe(mat, visited, i, j - 1):
        min_dist = findShortestPath(mat, visited, i, j - 1, x, y, min_dist, dist + 1)

    # backtrack: remove (i, j) from the visited matrix
    visited[i][j] = False
    return min_dist


# Wrapper over findShortestPath() function
def solution(mat):
    row = len(mat)
    col = len(mat[0])

    # construct an `M × N` matrix to keep track of visited
    # cells
    visited = []
    for i in range(row):
        visited.append([None for _ in range(col)])

    dist = sys.maxsize
    dist = findShortestPath(mat, visited, 0, 0, row, col, dist, 0)

    if dist != sys.maxsize:
        return dist
    return -1


# This code is contributed by phasing17
