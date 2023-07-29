def solution(original_string):
    """Given a non-empty string, it returns the maximum number
    of equal parts that the string can be cut into.

    Args:
        original_string (string): A string containing lower-case letters

    Returns:
        int: The maximum number of equal parts that it can be cut into.
    """

    max_cuts = 1
    for num_of_splits in range(1, int(len(original_string) + 1)):
        # if the string can be equally divided in num_of_splits parts
        if len(original_string) % num_of_splits == 0:
            substring_len = int(len(original_string) / num_of_splits)
            # Cyclical string consideration
            for offset in range(substring_len):
                temp_full_string = original_string[offset:] + original_string[0:offset]
                # get the first num_of_splits letters of the string in a substring
                substring = temp_full_string[0:substring_len]
                # Count the number of occurences of the substring in the full string
                number = temp_full_string.count(substring)
            # count the number of occurences of this substring in the full string
            # If the number of occurences equals the number of equal parts the string is cut into
            # And the number of occurences is bigger than the current max
            if number == num_of_splits and number > max_cuts:
                max_cuts = number  # update the max
    return max_cuts
