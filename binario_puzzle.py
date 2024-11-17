#!/usr/bin/env python3

import math
import subprocess

from args_parsing import parser
from puzzle_encoding import parse_input, encode_grouping, encode_line_uniqueness, encode_dot_counts


def encode_puzzle(input_file_path: str, output_file_path: str, verb: int):
    variables, puzzle_specific_clauses, size = parse_input(input_file_path)

    grouping_clauses = encode_grouping(variables)

    if verb > 0:
        print("1st rule encoded")

    uniqueness_clauses = encode_line_uniqueness(variables)
    if verb > 0:
        print("2nd rule encoded")

    dot_count_clauses = encode_dot_counts(variables)
    if verb > 0:
        print("3rd rule encoded")

    all_clauses = puzzle_specific_clauses + grouping_clauses + uniqueness_clauses + dot_count_clauses

    # write_cnf(dot_count_clauses,size*size, output_file_path)
    write_cnf(all_clauses, size * size, output_file_path)


def write_cnf(clauses: list[str], num_of_variables: int, output_file_path: str):
    with open(output_file_path, "a") as file:
        file.truncate(0)
        file.write(f"p cnf {num_of_variables} {len(clauses)}\n")
        for clause in clauses:
            file.write(f"\n{clause} 0")


def call_solver(input_file_path: str, solver_architecture: str, verbosity: int = 2) -> str:
    solver_path = ""
    if solver_architecture == "win":
        solver_path = "win_solver/glucose-syrup.exe"
    if solver_architecture == "unix":
        solver_path = "unix_solver/glucose_solver"
    if solver_path == "":
        raise Exception("Solver OS wrongly specified. \n use either \"win\" or \"unix\"")

    solver_result = subprocess.run(['./' + solver_path, '-model', '-verb=' + str(verbosity), input_file_path],
                                   stdout=subprocess.PIPE)

    result_line = ""
    for line in solver_result.stdout.decode('utf-8').split('\n'):
        if line.startswith('v'):
            result_line = line
        if verbosity > 0:
            print(line)

    return result_line


def human_readable_result(result: str):
    if result == "":
        print("Puzzle is unsolvable")
        return

    result = result[1:-2].strip().split()
    line_size = math.floor(math.sqrt(len(result)))

    print("-" * (line_size * 4 + 1))
    for i in range(line_size):
        line = ""
        for j in range(line_size):
            if result[i * line_size + j].startswith("-"):
                line += "| O "
            else:
                line += "| X "
        print(line + "|")
        print("-" * (line_size * 4 + 1))


def main(args):
    encode_puzzle(args.input, args.output, args.verb)

    result = call_solver(args.output, args.system, args.verb)

    human_readable_result(result)


if __name__ == '__main__':
    _args = parser.parse_args()

    main(_args)
