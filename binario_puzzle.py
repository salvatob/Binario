import math
import subprocess
from time import perf_counter

from puzzle_encoding import parse_input, encode_grouping, encode_line_uniqueness, encode_dot_counts


def encode_puzzle(input_file_path: str, output_file_path: str):
    variables, puzzle_specific_clauses, size = parse_input(input_file_path)

    grouping_clauses = encode_grouping(variables)
    print("encoded 1")

    uniqueness_clauses = encode_line_uniqueness(variables)
    print("encoded 2")

    dot_count_clauses = encode_dot_counts(variables)
    print("encoded 3")

    all_clauses = puzzle_specific_clauses + grouping_clauses + uniqueness_clauses + dot_count_clauses

    # write_cnf(dot_count_clauses,size*size, output_file_path)
    write_cnf(all_clauses,size*size, output_file_path)


def write_cnf(clauses : list[str], num_of_variables: int, output_file_path: str):
    with open(output_file_path, "a") as file:
        file.truncate(0)
        file.write(f"p cnf {num_of_variables} {len(clauses)}\n")
        for clause in clauses:
            file.write(f"\n{clause} 0")

def call_solver(input_file_path: str, verbosity: int = 2) -> str:
    result = subprocess.run(['./win_solver/glucose-syrup.exe', '-model', '-verb=' + str(verbosity), input_file_path],
                          stdout=subprocess.PIPE)
    for line in result.stdout.decode('utf-8').split('\n'):
        if line.startswith('v'):
            result_line = line
        print(line)
    return result_line

def human_readable_result(result: str):
    result = result[1:-2].strip().split()
    line_size = math.floor(math.sqrt(len(result)))

    for i in range(line_size):
        line = ""
        for j in range(line_size):
            if result[i * line_size+j].startswith("-"):
                line += "O "
            else:
                line += "X "
        print(line)


if __name__ == '__main__':
    t1_start = perf_counter()

    encode_puzzle( "input.txt", "output.cnf")

    print("encoded all")

    t1_stop = perf_counter()

    print(f"encoding took: {t1_stop - t1_start} ms")

    result = call_solver("output.cnf", 2)
    human_readable_result(result)
