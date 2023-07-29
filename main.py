from solution import solution
import pytest


def test_one_substring_many_times():
    assert 4 == solution("abcabcabcabc")


def test_one_substring_many_times():
    assert 2 == solution("abccbaabccba")


def test_cyclical_substring():
    assert 2 == solution("caabbccaabbc")


def test_one_character():
    assert 1 == solution("a")


def test_one_character_many_times():
    assert 4 == solution("aaaa")


def test_whole_string():
    assert 1 == solution("abcd")


def test_whole_string_odd():
    assert 2 == solution("abcdeabcde")


def test_whole_string_odd_once():
    assert 1 == solution("abcde")


def test_whole_string_odd_three_times():
    assert 3 == solution("abcabcabc")
