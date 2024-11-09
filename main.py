



def encode(whites, blacks, size: int):
    variables = [ [j + (i*size) + 1 for j in range(size)] for i in range(size)]
    return variables

def encode_row_uniqness(vars):
    ...

def encode_grouping(vars : list[list[int]]):
    # for any row/column, no more, than 2 same values can be next to eachother
    size = len(vars)
    clausules : list[str] = []

    for i in range(size):
        for j in range(size - 2):
            row_positive = f"{vars[i][j]} {vars[i][j+1]} {vars[i][j+2]}"
            row_negative = f"-{vars[i][j]} -{vars[i][j+1]} -{vars[i][j+2]}"
            clausules.append(row_positive)
            clausules.append(row_negative)

            column_positive = f"{vars[j][i]} {vars[j+1][i]} {vars[j+2][i]}"
            column_negative = f"-{vars[j][i]} -{vars[j+1][i]} -{vars[j+2][i]}"
            clausules.append(column_positive)
            clausules.append(column_negative)

    return clausules


if __name__ == '__main__':
    e = encode(0 ,0,4)
    p = encode_grouping(e)
    print(p)