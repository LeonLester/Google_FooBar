def solution(mat, path=[], curr_x=0, curr_y=0, have_flipped=False):
    print(f"{path=}, {curr_x=}, {curr_y=}")
    if (
        curr_x < 0
        or curr_x >= len(mat)
        or curr_y < 0
        or curr_y >= len(mat[0])  # out of bounds
        or ((curr_x, curr_y) in path)
        or (mat[curr_x][curr_y] == 1 and have_flipped)  # already visited
    ):  # visited wall after already flipped one
        return 0

    updated_path = path + [(curr_x, curr_y)]
    # reach the end
    if curr_x == len(mat) - 1 and curr_y == len(mat[0]) - 1:
        return len(updated_path)

    if not have_flipped and mat[curr_x][curr_y] == 1:
        have_flipped = True

    next_steps = [
        solution(mat, updated_path, curr_x, curr_y + 1, have_flipped),  # down
        solution(mat, updated_path, curr_x, curr_y - 1, have_flipped),  # up
        solution(mat, updated_path, curr_x + 1, curr_y, have_flipped),  # right
        solution(mat, updated_path, curr_x - 1, curr_y, have_flipped),  # left
    ]

    next_steps = [step for step in next_steps if step]
    if next_steps:
        return min(next_steps)
    else:
        return 0


# mat = [
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0],
# ]


# mat = [[0, 1, 1], [0, 0, 0], [1, 0, 0]]


mat = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0],
]


mat = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
# 41
print(solution(mat))
