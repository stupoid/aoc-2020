from day.eight.main import (
    print_history,
    run_modified_until_exit,
    run_until_loop_or_exit,
)


def test_run_until_loop_or_exit():
    input_file = open("day/eight/test_input.txt", "r")
    program = [l.strip() for l in input_file]
    history = run_until_loop_or_exit(program)
    print_history(history, program, show_line_no=True)
    assert history[-1][1] == 5


def test_run_modified_until_exit():
    input_file = open("day/eight/test_input.txt", "r")
    program = [l.strip() for l in input_file]
    history, modified_program = run_modified_until_exit(program)
    print_history(history, modified_program, show_line_no=True)
    assert history[-1][1] == 8
