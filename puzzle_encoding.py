def parse_input(input_file_path : str) -> tuple[list[list[int]], list[str], int]:
    positive_literal = 'X'
    negative_literal = 'O'

    clauses = []
    with open(input_file_path, "r") as file:

        lines = file.read().strip().split("\n")
        n = len(lines[0].strip())
        if n % 2 != 0 or n == 0:
            raise Exception("Input file must have even nonzero number of symbols on each line")
        if len(lines) != n:
            raise Exception("Input file doesnt have same number of lines as symbols on first line")

        puzzle_size = len(lines)
        if lines[-1] == "":
            puzzle_size -= 1

        variables = create_logical_variables(puzzle_size)

        for  line, row in zip(lines, variables):
            if len(line.strip()) != n:
                raise Exception("Input file must have same number of symbols on each line")

            for i, char in enumerate(line.upper()):
                if char == positive_literal:
                    clauses.append(f"{row[i]}")
                if char == negative_literal:
                    clauses.append(f"-{row[i]}")

    return variables, clauses, puzzle_size

def get_matrix_column(matrix :list[list[int]], column_index : int)-> list[int]:
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_index])
    return column

def create_logical_variables(size: int) -> list[list[int]]:
    # each logical variable is encoded as an int, accessed exclusively through an array
    # using standard array coordinates (indexes)
    variables = [ [j + (i*size) + 1 for j in range(size)] for i in range(size)]
    return variables

def encode_line_uniqueness(variables : list[list[int]]):
    size = len(variables)
    clauses = []
    for i in range(size):
        for j in range(i+1, size):
            clauses += (compare_rows(variables, i,j))
            clauses += (compare_columns(variables, i,j))
    return clauses

def compare_rows(variables : list[list[int]], row1 : int, row2 : int) -> list[str]:
    variables_first = variables[row1]
    variables_second = variables[row2]
    statements = []

    recursively_encode_lines(0, variables_first, variables_second, "", statements)

    return statements

def compare_columns(variables : list[list[int]], column1 : int, column2 : int) -> list[str]:
    size = len(variables)

    variables_first = []
    variables_second = []

    for i in range(size):
        variables_first.append(variables[i][column1])
        variables_second.append(variables[i][column2])

    statements = []

    recursively_encode_lines(0, variables_first, variables_second, "", statements)

    return statements

def recursively_encode_lines(current_depth: int, variables_1 : list[int], variables_2 : list[int], current_clause : str, clausules : list[str]):
    if current_depth >= len(variables_1):
        clausules.append(current_clause)
        return
    new_additions = [
        f" {variables_1[current_depth]} {variables_2[current_depth]}",
        f" -{variables_1[current_depth]} -{variables_2[current_depth]}"
    ]
    for each_var in new_additions:
        new_bracket = current_clause + each_var
        recursively_encode_lines(current_depth +1,variables_1, variables_2, new_bracket, clausules)

def encode_grouping(variables : list[list[int]]) -> list[str]:
    # for any row/column, no more, than 2 same values can be next to each other
    # equivalent with: for each three dots, that are directly next to each other vertically or diagonally
    # one must be different
    size = len(variables)
    clauses : list[str] = []

    for i in range(size):
        for j in range(size - 2):
            row_positive = f"{variables[i][j]} {variables[i][j + 1]} {variables[i][j + 2]}"
            row_negative = f"-{variables[i][j]} -{variables[i][j + 1]} -{variables[i][j + 2]}"
            clauses.append(row_positive)
            clauses.append(row_negative)

            column_positive = f"{variables[j][i]} {variables[j + 1][i]} {variables[j + 2][i]}"
            column_negative = f"-{variables[j][i]} -{variables[j + 1][i]} -{variables[j + 2][i]}"
            clauses.append(column_positive)
            clauses.append(column_negative)

    return clauses

def encode_dot_counts(variables: list[list[int]]) -> list[str]:
    clauses: list[str] = []

    for row in variables:
        clauses += encode_line_dot_count(row)

    for i in range(len(variables)):
        column = get_matrix_column(variables, i)
        clauses += encode_line_dot_count(column)

    return clauses

def encode_line_dot_count(line: list[int])-> list[str]:
    clauses: list[str] = []

    recurse_dot_count(line, 0, "", clauses)

    return clauses

def recurse_dot_count(line: list[int], current_depth: int, current_clause: str , clauses : list[str]):
    if current_depth >= len(line):
        if check_if_illegal(current_clause):
            clauses.append(current_clause)
        return

    new_clause_1 = current_clause + str(line[current_depth]) + " "
    new_clause_2 = current_clause + "-" +str(line[current_depth]) + " "

    recurse_dot_count(line, current_depth + 1, new_clause_1, clauses)
    recurse_dot_count(line, current_depth + 1, new_clause_2, clauses)

def check_if_illegal(line: str) -> bool:
    tokens = line.strip().split(" ")
    positive = negative = 0
    for token in tokens:
        if token.startswith("-"):
            negative += 1
        else:
            positive += 1
    return positive != negative
