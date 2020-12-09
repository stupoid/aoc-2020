"""
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

To begin, get your puzzle input. https://adventofcode.com/2020/day/8/input

--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?


"""
from typing import List, Optional, Tuple


def print_history(
    history: List[Tuple[int, int]], program: List[str], show_line_no: bool = False
):
    step_history = {}
    for step, (i, acc) in enumerate(history, 1):
        if i not in step_history:
            step_history[i] = []
        step_history[i].append(str(step))

    last_i = history[-1][0]

    for i, line in enumerate(program):
        output = ""
        if show_line_no:
            output += f"{i+1:3}: "

        if i == last_i:
            step_history[i][-1] += "(!)"

        output += f"{line:8}| {', '.join(step_history.get(i, [])):8}"
        print(output)

    if last_i < len(program):
        print(f"loop detected at line: {last_i+1}")
    else:
        print("program exit")


def parse(line: str) -> Tuple[str, int]:
    op, arg = line.split(" ")
    arg = int(arg)
    return op, arg


def modify_line(line: str) -> str:
    if line.startswith("nop"):
        return line.replace("nop", "jmp")
    elif line.startswith("jmp"):
        return line.replace("jmp", "nop")


def modify_program(program: List[str], line_no: int) -> List[str]:
    modified_program = program.copy()
    modified_program[line_no] = modify_line(modified_program[line_no])
    return modified_program


def run_until_loop_or_exit(
    program: List[str], history: List[Tuple[int, int]] = []
) -> List[Tuple[int, int]]:
    i, acc = history[-1] if len(history) else (0, 0)
    visited = {i for i, _ in history}

    while i < len(program):
        visited.add(i)
        op, arg = parse(program[i])
        i, acc = next_state(i, acc, op, arg)
        history.append((i, acc))

        if i in visited:
            break

    return history


def run_modified_until_exit(
    program: List[str],
) -> Optional[Tuple[List[Tuple[int, int]], List[str]]]:
    history = run_until_loop_or_exit(program=program)
    i, _ = history[-1]
    if i > len(program) - 1:
        return history, program

    for index in range(len(history) - 1, 0, -1):
        i, _ = history[index]
        if program[i].startswith("nop") or program[i].startswith("jmp"):
            modified_program = modify_program(program, i)
            modified_history = run_until_loop_or_exit(modified_program, history[:index])
            exit_i, _ = modified_history[-1]
            if exit_i > len(modified_program) - 1:
                return modified_history, modified_program


def next_state(i: int, acc: int, op: str, arg: int) -> Tuple[int, int]:
    if op == "nop":
        i += 1
    elif op == "acc":
        acc += arg
        i += 1
    elif op == "jmp":
        i += arg
    return i, acc


def main():
    input_file = open("day/eight/input.txt", "r")
    program = [l.strip() for l in input_file]
    history = run_until_loop_or_exit(program)
    i, acc = history[-1]
    # print_history(history, program)
    print(f"value in accumulator: {acc}")

    history, modified_program = run_modified_until_exit(program)
    i, acc = history[-1]
    # print_history(history, modified_program)
    print(f"value in accumulator: {acc}")


if __name__ == "__main__":
    main()
