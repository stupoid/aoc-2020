from day.ten.main import (
    get_adapter_rating,
    get_jolt_differences,
    possible_arrangements,
)


def test_get_adapter_rating():
    assert get_adapter_rating([3, 9, 6], 3) == 12

    input_file = open("day/ten/test_input.txt", "r")
    input_list = [int(i) for i in input_file]
    assert get_adapter_rating(input_list, 3) == 22


def test_get_jolt_differences():
    input_file = open("day/ten/test_input.txt", "r")
    input_list = [int(i) for i in input_file]
    assert get_jolt_differences(input_list) == {1: 7, 3: 5}

    input_file = open("day/ten/test_input_2.txt", "r")
    input_list = [int(i) for i in input_file]
    assert get_jolt_differences(input_list) == {1: 22, 3: 10}


def test_possible_arrangements():
    input_file = open("day/ten/test_input.txt", "r")
    input_list = [int(i) for i in input_file]
    assert possible_arrangements(input_list) == 8

    input_file = open("day/ten/test_input_2.txt", "r")
    input_list = [int(i) for i in input_file]
    assert possible_arrangements(input_list) == 19208
