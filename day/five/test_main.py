from day.five.main import find_missing_int, get_col, get_id, get_row


def test_get_row():
    input_file = open("day/five/test_input.txt", "r")
    input_list = list(input_file)
    assert get_row(input_list[0]) == 44
    assert get_row(input_list[1]) == 70
    assert get_row(input_list[2]) == 14
    assert get_row(input_list[3]) == 102


def test_get_col():
    input_file = open("day/five/test_input.txt", "r")
    input_list = list(input_file)
    assert get_col(input_list[0]) == 5
    assert get_col(input_list[1]) == 7
    assert get_col(input_list[2]) == 7
    assert get_col(input_list[3]) == 4


def test_get_id():
    input_file = open("day/five/test_input.txt", "r")
    input_list = list(input_file)
    assert get_id(input_list[0]) == 357
    assert get_id(input_list[1]) == 567
    assert get_id(input_list[2]) == 119
    assert get_id(input_list[3]) == 820


def test_find_missing_int():
    test_list = [2, 4]
    assert find_missing_int(test_list) == 3

    test_list = [2, 3, 4, 6, 7]
    assert find_missing_int(test_list) == 5

    test_list = [2, 4, 5, 6, 7]
    assert find_missing_int(test_list) == 3

    test_list = [3, 4, 5, 7]
    assert find_missing_int(test_list) == 6

    test_list = [98, 100]
    assert find_missing_int(test_list) == 99

    test_list = [5]
    assert find_missing_int(test_list) == 6
