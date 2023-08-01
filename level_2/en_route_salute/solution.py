def solution(sequence):
    """Given a string that corresponds to the positions and
    directions of people in a corridor, calculates the number of interactions that will occur.
    One intersection of two people counts as two interactions

    Args:
        sequence (string): The layout of the corridor expressed with <,>,-

    Returns:
        int: The number of interactions that will occur
    """

    salutes = 0
    flag = False
    right_count = 0
    for position in sequence:
        print(position)
        if position == ">":
            flag = True
            right_count += 1
        if flag and position == "<":
            salutes += 2 * right_count
    return salutes
