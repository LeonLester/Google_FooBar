def solution(original_string):
    """Given a non-empty string, it returns the maximum number
    of equal parts that the string can be cut into.

    Args:
        original_string (string): A string containing lower-case letters

    Returns:
        int: The maximum number of equal parts that it can be cut into.
    """

    max_cuts = 1
    for num_of_splits in range(1, len(original_string) + 1):
        # Divide the string into num_of_splits equal parts
        substring_len = int(len(original_string) / num_of_splits)
        # print(f"========= {substring_len=} =========")
        # Get a substring starting at different characters from the left
        for offset in range(substring_len):
            # print(
            #     f"{original_string[offset:]} - {original_string[0:offset]} - {offset=}"
            # )
            # Add the first characters we skipped, to the end of the string
            temp_full_string = original_string[offset:] + original_string[0:offset]
            # Get the substring at the start of the new string
            substring = temp_full_string[0:substring_len]
            # get the first num_of_splits letters of the string in a substring
            number = temp_full_string.count(substring)
            # print(f"{number=} {num_of_splits=}")
            # count the number of occurences of this substring in the full string
            # If the number of occurences equals the number of equal parts the string is cut into
            # And the number of occurences is bigger than the current max
            if number == num_of_splits and number > max_cuts:
                max_cuts = number  # update the max
            # print(max_cuts)
    return max_cuts
