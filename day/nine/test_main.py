from day.nine.main import find_contiguous_sum, find_invalid, next_numbers


def test_next_numbers():
    input_list = [i for i in range(1, 26)]
    possible_numbers = list(next_numbers(input_list[-25:]))
    assert 26 in possible_numbers
    assert 49 in possible_numbers
    assert 100 not in possible_numbers
    assert 50 not in possible_numbers

    input_list.append(45)
    input_list[0] = 20
    input_list[19] = 1
    possible_numbers = list(next_numbers(input_list[-25:]))
    assert 26 in possible_numbers
    assert 65 not in possible_numbers
    assert 64 in possible_numbers
    assert 66 in possible_numbers

    input_file = open("day/nine/test_input.txt", "r")
    input_list = [int(i) for i in input_file]
    assert input_list[5] in next_numbers(input_list[:5])


def test_find_invalid():
    input_file = open("day/nine/test_input.txt", "r")
    input_list = [int(i) for i in input_file]
    assert find_invalid(input_list, 5) == 127


def test_find_contiguous_sum():
    input_file = open("day/nine/test_input.txt", "r")
    input_list = [int(i) for i in input_file]
    assert find_contiguous_sum(input_list, 127) == (15, 47)
