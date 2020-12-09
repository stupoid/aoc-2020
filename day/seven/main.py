"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

To begin, get your puzzle input. https://adventofcode.com/2020/day/7/input

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

import re
from typing import Dict, List, NewType, Set, Tuple, Union

Rule = NewType("Rule", List[Union[str, Tuple[int, str]]])


def parse(line: str) -> Rule:
    results = re.findall(r"((?:\d+\s)*\b(?!no other\b)\w+\s\w+(?=\sbag))", line)
    rule = [results[0]]
    for r in results[1:]:
        amount, color = r.split(" ", 1)
        rule.append((int(amount), color))
    return rule


def generate_lookup(rules: List[Rule]) -> Dict[str, Dict[str, int]]:
    lookup_table = {}
    for rule in rules:
        bag = rule[0]
        if len(rule[1:]):
            lookup_table[bag] = {c: int(i) for i, c in rule[1:]}
        else:
            lookup_table[bag] = 0
    return lookup_table


def generate_reverse_lookup(rules) -> Dict[str, Dict[str, int]]:
    lookup_table = {}
    for rule in rules:
        bag = rule[0]
        for amt, color in rule[1:]:
            lookup_table[color] = lookup_table.get(color, {})
            lookup_table[color][bag] = amt
    return lookup_table


def find_bag(color: str, lookup_table: Dict[str, Dict[str, int]]) -> Set[str]:
    lookup_table = {k: list(v) for k, v in lookup_table.items()}
    colors = lookup_table.get(color, [])
    for c in colors:
        colors += lookup_table.get(c, [])
    return set(colors)


def get_bags_in_bag(bag: str, lookup_table: Dict[str, Dict[str, int]]) -> int:
    contents = lookup_table.get(bag, 0)
    if contents == 0:
        return 0

    return sum(
        (v + (v * get_bags_in_bag(k, lookup_table)) for k, v in contents.items())
    )


def main():
    input_file = open("day/seven/input.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    reverse_lookup_table = generate_reverse_lookup(rules)
    result = len(find_bag("shiny gold", reverse_lookup_table))

    print(f"bags that can eventually contain at least one shiny gold bag: {result}")

    lookup_table = generate_lookup(rules)
    result = get_bags_in_bag("shiny gold", lookup_table)
    print(f"individual bags required inside shiny gold bag: {result}")


if __name__ == "__main__":
    main()
