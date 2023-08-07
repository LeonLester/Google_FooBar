# Python3 code to implement the approach
import sys


# User defined Pair class
class Pair:
    def __init__(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y


HAVE_REMOVED_WALL = {"bool": False}


# Check if it is possible to go to (target_x, target_y) from the current
# position. The function returns false if the cell has
# value 0 or already visited
def isSafe(mat, visited, target_x, target_y):
    # print(f"isSafe: {target_x},{target_y}")
    standard_checks = (
        target_x >= 0
        and target_x < len(mat)
        and target_y >= 0
        and target_y < len(mat[0])
        and (not visited[target_x][target_y])
    )

    if standard_checks and (mat[target_x][target_y] == 0):
        return True

    elif (
        standard_checks
        and mat[target_x][target_y] == 1
        and not HAVE_REMOVED_WALL["bool"]
    ):
        HAVE_REMOVED_WALL["bool"] = True
        return True

    elif standard_checks and (
        mat[target_x][target_y] == 1 and HAVE_REMOVED_WALL["bool"]
    ):
        return False


def findShortestPath(mat, visited, curr_x, curr_y, target_x, target_y, min_dist, dist):
    # print(
    #     f"findShortestPath with: ({curr_x},{curr_y}) ({target_x},{target_y}) {min_dist}, {dist}"
    # )
    if curr_x == target_x and curr_y == target_y:
        min_dist = min(dist, min_dist)
        return min_dist

    # set (curr_x, curr_y) cell as visited
    visited[curr_x][curr_y] = True

    # go to the bottom cell
    if isSafe(mat, visited, curr_x + 1, curr_y):
        min_dist = findShortestPath(
            mat, visited, curr_x + 1, curr_y, target_x, target_y, min_dist, dist + 1
        )

    # go to the right cell
    if isSafe(mat, visited, curr_x, curr_y + 1):
        min_dist = findShortestPath(
            mat, visited, curr_x, curr_y + 1, target_x, target_y, min_dist, dist + 1
        )

    # go to the top cell
    if isSafe(mat, visited, curr_x - 1, curr_y):
        min_dist = findShortestPath(
            mat, visited, curr_x - 1, curr_y, target_x, target_y, min_dist, dist + 1
        )

    # go to the left cell
    if isSafe(mat, visited, curr_x, curr_y - 1):
        min_dist = findShortestPath(
            mat, visited, curr_x, curr_y - 1, target_x, target_y, min_dist, dist + 1
        )

    # backtrack: remove (curr_x, curr_y) from the visited matrix
    visited[curr_x][curr_y] = False
    return min_dist


# Wrapper over findShortestPath() function
def solution(mat):
    # if len(mat) == 0:
    #     print("haaa")
    #     return -1

    row = len(mat)
    col = len(mat[0])
    src = Pair(0, 0)
    dest = Pair(len(mat) - 1, len(mat[0]) - 1)

    # construct an `M × N` matrix to keep track of visited
    # cells
    visited = []
    for _ in range(row):
        visited.append([None for _ in range(col)])

    dist = sys.maxsize
    # print(f"here2, {src.target_x}, {src.target_y}, {dest.target_x}, {dest.target_y}, {dist}")
    dist = findShortestPath(
        mat, visited, src.target_x, src.target_y, dest.target_x, dest.target_y, dist, 1
    )

    # if dist != sys.maxsize:
    return dist
    # print(f"Dist is equal to maxsize")
    # return -1
