import functools
from operator import mul

from day.one.main import find_entries_that_sum_to


def test_find_two_entries_that_sum_to_2020():
    input_file = open("day/one/test_input.txt", "r")
    entry_list = [int(l) for l in input_file]
    entries = find_entries_that_sum_to(entry_list, 2, 2020)
    assert entries == (1721, 299)
    assert functools.reduce(mul, entries) == 514579


def test_find_three_entries_that_sum_to_2020():
    input_file = open("day/one/test_input.txt", "r")
    entry_list = [int(l) for l in input_file]
    entries = find_entries_that_sum_to(entry_list, 3, 2020)
    assert entries == (979, 366, 675)
    assert functools.reduce(mul, entries) == 241861950
