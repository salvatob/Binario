def parse_input(input_file_path : str) -> tuple[list[list[int]], list[str], int]:
    positive_literal = 'X'
    negative_literal = 'O'
    unknown_literal = '_'

    clauses = []
    with open(input_file_path, "r") as file:

        lines = file.readlines()


        # print("lines")
        # for line in lines:
        #     print(line)
        #
        # print("------")
        puzzle_size = len(lines)
        if lines[-1] == "":
            puzzle_size -= 1

        variables = create_logical_variables(puzzle_size)

        for  line, row in zip(lines, variables):
            for i, char in enumerate(line):
                if char == positive_literal:
                    clauses.append(f"{row[i]}")
                if char == negative_literal:
                    clauses.append(f"-{row[i]}")

    return variables, clauses, puzzle_size

def create_logical_variables(size: int) -> list[list[int]]:
    # each logical variable is encoded as an int, accessed exclusively through an array
    # using standard array coordinates (indexes)
    variables = [ [j + (i*size) + 1 for j in range(size)] for i in range(size)]
    return variables

def encode_row_uniqueness(variables : list[list[int]]):
    size = len(variables)
    for i in range(size):
        for j in range(i+1, size):
            compare_rows(variables, i,j)


def compare_rows(variables : list[list[int]], row1 : int, row2 : int):
    # size = len(variables)
    variables_first = variables[row1]
    variables_second = variables[row2]
    statements = []

    recursively_encode_lines(variables,0, variables_first, variables_second, "", statements)

    return statements


def recursively_encode_lines(variables : list[list[int]], current_depth: int, variables_1 : list[int] , variables_2 : list[int], current_bracket : str, clausules : list[str]):
    if current_depth >= len(variables_1):
        clausules.append(current_bracket)
        return
    new_additions = [
        f" {variables_1[current_depth]} {variables_2[current_depth]}",
        f" -{variables_1[current_depth]} -{variables_2[current_depth]}"
    ]
    for each_var in new_additions:
        new_bracket = current_bracket + each_var
        recursively_encode_lines(variables, current_depth + 1, variables_1, variables_2, new_bracket, clausules)


def encode_grouping(variables : list[list[int]]):
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


if __name__ == '__main__':
    e = encode(4)
    # p = encode_grouping(e)
    # print(p)

    r = compare_rows(e,0,1)
    for x in r:
        print(x)

    # parse_input("", "ff")
    # encode_row_uniqueness(e)
    #
    # s = "123"
    # p = s
    # p += "4"
    # print(s)
    # print(p)