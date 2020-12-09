from day.seven.main import (
    generate_lookup,
    generate_reverse_lookup,
    get_bags_in_bag,
    parse,
    find_bag,
)


def test_parse():
    input_file = open("day/seven/test_input.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    assert rules == [
        ["light red", (1, "bright white"), (2, "muted yellow")],
        ["dark orange", (3, "bright white"), (4, "muted yellow")],
        ["bright white", (1, "shiny gold")],
        ["muted yellow", (2, "shiny gold"), (9, "faded blue")],
        ["shiny gold", (1, "dark olive"), (2, "vibrant plum")],
        ["dark olive", (3, "faded blue"), (4, "dotted black")],
        ["vibrant plum", (5, "faded blue"), (6, "dotted black")],
        ["faded blue"],
        ["dotted black"],
    ]


def test_generate_lookup():
    input_file = open("day/seven/test_input.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    assert generate_lookup(rules) == {
        "light red": {"bright white": 1, "muted yellow": 2},
        "dark orange": {"bright white": 3, "muted yellow": 4},
        "bright white": {"shiny gold": 1},
        "muted yellow": {"shiny gold": 2, "faded blue": 9},
        "shiny gold": {"dark olive": 1, "vibrant plum": 2},
        "dark olive": {"faded blue": 3, "dotted black": 4},
        "vibrant plum": {"faded blue": 5, "dotted black": 6},
        "faded blue": 0,
        "dotted black": 0,
    }


def test_generate_reverse_lookup():
    input_file = open("day/seven/test_input.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    assert generate_reverse_lookup(rules) == {
        "bright white": {"light red": 1, "dark orange": 3},
        "muted yellow": {"light red": 2, "dark orange": 4},
        "shiny gold": {"bright white": 1, "muted yellow": 2},
        "faded blue": {"muted yellow": 9, "dark olive": 3, "vibrant plum": 5},
        "dark olive": {"shiny gold": 1},
        "vibrant plum": {"shiny gold": 2},
        "dotted black": {"dark olive": 4, "vibrant plum": 6},
    }


def test_find_bag():
    input_file = open("day/seven/test_input.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    assert find_bag("shiny gold", generate_reverse_lookup(rules)) == {
        "bright white",
        "muted yellow",
        "dark orange",
        "light red",
    }

    assert find_bag("dark olive", generate_reverse_lookup(rules)) == {
        "shiny gold",
        "bright white",
        "muted yellow",
        "dark orange",
        "light red",
    }


def test_count_bags():
    input_file = open("day/seven/test_input.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    lookup_table = generate_lookup(rules)
    assert get_bags_in_bag("dark olive", lookup_table) == 7
    assert get_bags_in_bag("faded blue", lookup_table) == 0
    assert get_bags_in_bag("vibrant plum", lookup_table) == 11
    assert get_bags_in_bag("shiny gold", lookup_table) == 32

    input_file = open("day/seven/test_input_2.txt", "r")
    rules = [parse(i.strip()) for i in input_file]
    lookup_table = generate_lookup(rules)
    assert get_bags_in_bag("shiny gold", lookup_table) == 126