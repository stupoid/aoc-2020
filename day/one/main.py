"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

To begin, get your puzzle input. https://adventofcode.com/2020/day/1/input

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

import functools
import itertools
from operator import mul
from typing import Iterable, Optional, Tuple


def find_entries_that_sum_to(
    input: Iterable[int],
    num_entries: int,
    sum_to: int,
) -> Optional[Tuple[int]]:
    combinations = itertools.combinations(input, num_entries)
    for entries in combinations:
        if sum(entries) == sum_to:
            return entries


def main():
    input_file = open("day/one/input.txt", "r")
    entry_list = [int(l) for l in input_file]
    n = 2
    sum_to = 2020

    if entries := find_entries_that_sum_to(entry_list, n, sum_to):
        product_of_entries = functools.reduce(mul, entries)
        print(f"product of {n} entries that sum to {sum_to}: {product_of_entries}")
    else:
        print(f"product of {n} entries that sum to {sum_to} not found")

    n = 3

    if entries := find_entries_that_sum_to(entry_list, n, sum_to):
        product_of_entries = functools.reduce(mul, entries)
        print(f"product of {n} entries that sum to {sum_to}: {product_of_entries}")
    else:
        print(f"product of {n} entries that sum to {sum_to} not found")


if __name__ == "__main__":
    main()
