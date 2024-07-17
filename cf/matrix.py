

def matrix_center():
    column_position = 0
    row_position = 0

    for i in range(5):
        row = list(map(int, input().split()))
        if 1 in row:
            column_position = row.index(1) + 1
            row_position = i + 1
    
    moves_required = abs(column_position - 3) + abs (row_position - 3)

    return moves_required


print(matrix_center())


