from day.six.main import count_answers, count_consensus, process_groups


def test_process_groups():
    input_file = open("day/six/test_input.txt", "r")
    groups = [i for i in process_groups(input_file)]

    assert len(groups) == 5


def test_count_answers():
    input_file = open("day/six/test_input.txt", "r")
    total_count = sum([count_answers(i) for i in process_groups(input_file)])

    assert total_count == 11


def test_count_consensus():
    input_file = open("day/six/test_input.txt", "r")
    total_consensus = sum([count_consensus(i) for i in process_groups(input_file)])

    assert total_consensus == 6
