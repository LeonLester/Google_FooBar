# These are not the test cases of the website.
# They are the ones I could create that helped me.
from solution import solution


def test_one():
    assert ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"] == solution(
        ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    )


def test_two():
    assert ["1.0","1.0.2","1.0.12","1.1.2","1.3.3"] = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
