# These are not the test cases of the website.
# They are the ones I could create that helped me.
from solution import solution


def test_one_intersection():
    assert 2 == solution(">----<")


def test_two_intersections():
    assert 4 == solution("<<>><")


def test_no_intersections():
    assert 0 == solution("<>")


def test_multiple():
    assert 18 == solution(">>><<<")


def test_two_characters_interchange_multiple_times():
    assert 6 == solution("><><")
