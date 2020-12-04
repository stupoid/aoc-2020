from day.two.main import Policy, is_valid_password, rule, rule_2, process_line


def test_process_line():
    input_file = open("day/two/test_input.txt", "r")
    po_pw_list = [process_line(l) for l in input_file]

    assert po_pw_list == [
        (Policy(1, 3, "a"), "abcde"),
        (Policy(1, 3, "b"), "cdefg"),
        (Policy(2, 9, "c"), "ccccccccc"),
    ]


def test_valid_password():
    input_file = open("day/two/test_input.txt", "r")
    po_pw_list = [process_line(l) for l in input_file]

    assert is_valid_password(*po_pw_list[0], rule)
    assert is_valid_password(*po_pw_list[2], rule)


def test_invalid_password():
    input_file = open("day/two/test_input.txt", "r")
    po_pw_list = [process_line(l) for l in input_file]

    assert not is_valid_password(*po_pw_list[1], rule)


def test_valid_password2():
    input_file = open("day/two/test_input.txt", "r")
    po_pw_list = [process_line(l) for l in input_file]

    assert is_valid_password(*po_pw_list[0], rule_2)


def test_invalid_password():
    input_file = open("day/two/test_input.txt", "r")
    po_pw_list = [process_line(l) for l in input_file]

    assert not is_valid_password(*po_pw_list[1], rule_2)
    assert not is_valid_password(*po_pw_list[2], rule_2)
