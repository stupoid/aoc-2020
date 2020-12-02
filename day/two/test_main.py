from day.two.main import Policy, is_valid_password, is_valid_password2, process_line

test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def test_process_line():
    policy, password = process_line(test_input[0])

    assert isinstance(policy, Policy)
    assert isinstance(password, str)


def test_valid_password():
    policy, password = process_line(test_input[0])
    assert is_valid_password(policy, password)

    policy, password = process_line(test_input[2])
    assert is_valid_password(policy, password)


def test_invalid_password():
    policy, password = process_line(test_input[1])
    assert is_valid_password(policy, password) is False


def test_valid_password2():
    policy, password = process_line(test_input[0])
    assert is_valid_password2(policy, password)


def test_invalid_password():
    policy, password = process_line(test_input[2])
    assert is_valid_password2(policy, password) is False

    policy, password = process_line(test_input[1])
    assert is_valid_password2(policy, password) is False
