import math


def parse_input(whites: str, blacks: str):
    size = len(whites)
    if len(blacks) != size or math.isqrt(size)**2 != size:
        raise ValueError(f"invalid input")
    clauses = []

def encode( size: int) -> list[list[int]]:
    # each logical variable is encoded as an int, accessed exclusively through an array
    # using standard array coordinates (indexes)
    variables = [ [j + (i*size) + 1 for j in range(size)] for i in range(size)]
    return variables

def encode_row_uniqness(vars):
    ...

def encode_grouping(vars : list[list[int]]):
    # for any row/column, no more, than 2 same values can be next to eachother
    size = len(vars)
    clausules : list[str] = []

def encode_grouping(variables : list[list[int]]):
    # for any row/column, no more, than 2 same values can be next to each other
    # equivalent with: for each three dots, that are directly next to each other vertically or diagonally
    # one must be different
    size = len(variables)
    clauses : list[str] = []

    for i in range(size):
        for j in range(size - 2):
            row_positive = f"{variables[i][j]} {variables[i][j + 1]} {variables[i][j + 2]} 0"
            row_negative = f"-{variables[i][j]} -{variables[i][j + 1]} -{variables[i][j + 2]} 0"
            clauses.append(row_positive)
            clauses.append(row_negative)

            column_positive = f"{variables[j][i]} {variables[j + 1][i]} {variables[j + 2][i]} 0"
            column_negative = f"-{variables[j][i]} -{variables[j + 1][i]} -{variables[j + 2][i]} 0"
            clauses.append(column_positive)
            clauses.append(column_negative)

    return clauses


if __name__ == '__main__':
    e = encode(0 ,0,4)
    p = encode_grouping(e)
    print(p)