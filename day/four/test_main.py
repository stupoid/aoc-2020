from day.four.main import is_valid_passport, process_input, rules, rules_2


def test_process_input():
    input_file = open("day/four/test_input.txt", "r")
    processed_list = [i for i in process_input(input_file)]
    assert processed_list == [
        {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        },
        {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        },
        {
            "hcl": "#ae17e1",
            "iyr": "2013",
            "eyr": "2024",
            "ecl": "brn",
            "pid": "760753108",
            "byr": "1931",
            "hgt": "179cm",
        },
        {
            "hcl": "#cfa07d",
            "eyr": "2025",
            "pid": "166559648",
            "iyr": "2011",
            "ecl": "brn",
            "hgt": "59in",
        },
    ]


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
