from day.four.main import is_valid_passport, process_input, rules, rules_2


def test_process_input():
    input_file = open("day/four/test_input.txt", "r")
    assert len([i for i in process_input(input_file)]) == 4


def test_validate_passport_1():
    input_file = open("day/four/test_input.txt", "r")
    processed_list = [i for i in process_input(input_file)]
    assert sum(is_valid_passport(i, rules) for i in processed_list) == 2


def test_validate_valid_passports_2():
    input_file = open("day/four/valid_test_input.txt", "r")
    processed_list = [i for i in process_input(input_file)]
    assert all([is_valid_passport(i, rules_2) for i in processed_list])


def test_validate_invalid_passports_2():
    input_file = open("day/four/invalid_test_input.txt", "r")
    processed_list = [i for i in process_input(input_file)]
    assert all([not is_valid_passport(i, rules_2) for i in processed_list])
