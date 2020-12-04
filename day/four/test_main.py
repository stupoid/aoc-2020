from day.four.main import is_valid_passport, process_input, rules, rules_2

valid_passport = {
    "pid": "087499704",
    "hgt": "74in",
    "ecl": "grn",
    "iyr": "2012",
    "eyr": "2030",
    "byr": "1980",
    "hcl": "#623a2f",
}


def test_process_input():
    input_file = open("day/four/test_input.txt", "r")
    assert len([i for i in process_input(input_file)]) == 4


def test_validate_passport_1():
    input_file = open("day/four/test_input.txt", "r")
    assert sum(is_valid_passport(i, rules) for i in process_input(input_file)) == 2


def test_validate_valid_passports_2():
    input_file = open("day/four/valid_test_input.txt", "r")
    assert all([is_valid_passport(i, rules_2) for i in process_input(input_file)])


def test_validate_invalid_passports_2():
    input_file = open("day/four/invalid_test_input.txt", "r")
    assert all([not is_valid_passport(i, rules_2) for i in process_input(input_file)])
