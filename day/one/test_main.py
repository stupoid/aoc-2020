import functools
from operator import mul

from day.one.main import find_entries_that_sum_to

test_input = [1721, 979, 366, 299, 675, 1456]


def test_find_two_entries_that_sum_to_2020():
    entries = find_entries_that_sum_to(test_input, 2, 2020)
    assert entries == (1721, 299)
    assert functools.reduce(mul, entries) == 514579


def test_find_three_entries_that_sum_to_2020():
    entries = find_entries_that_sum_to(test_input, 3, 2020)
    assert entries == (979, 366, 675)
    assert functools.reduce(mul, entries) == 241861950
