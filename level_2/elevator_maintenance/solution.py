class Version:
    def __init__(self, major, minor=-1, patch=-1):
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)


def solution(pile):
    """Given a list of string that describe versions with major.minor.patch numbers,
    where only the major version is mandatory to exist, this function sorts them in ascending order
    Args:
        pile (list): The layout of the corridor expressed with <,>,-

    Returns:
        int: The list of the versions as strings, sorted.
    """

    objects = [Version(*item.split(".")) for item in pile]
    new_objects = sorted(objects, key=lambda x: ([x.major, x.minor, x.patch]))

    final_list = []
    for version in new_objects:
        to_add = str(version.major)
        if version.minor != -1:
            to_add = "{}.{}".format(to_add, version.minor)
            if version.patch != -1:
                to_add = "{}.{}".format(to_add, version.patch)
        final_list.append(to_add)

    return final_list
    # if len(pile) <= 1:
    #     return pile
    # else:
    #     pivot = pile[0]
    #     left = [x for x in pile[1:] if x < pivot]
    #     right = [x for x in pile[1:] if x >= pivot]
    #     return solution(left) + [pivot] + solution(right)
