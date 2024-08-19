
def matrix():

    row = -1
    column = -1

    for i in range(0,5):
        mat = list(map(int, input().split(' '))) 
        for j in range(0,5):
            if mat[j] == 1:
                row = i+1
                column = j+1

    ans = abs(3-row) + abs (3-column)

    return ans


print(matrix())

# ideal solution
# def matrix():
#     row, column = -1, -1

#     for i in range(5):
#         mat = list(map(int, input().split()))
#         if 1 in mat:
#             row, column = i, mat.index(1)

#     # The target position for 1 is at (2, 2) in 0-indexed matrix
#     moves = abs(2 - row) + abs(2 - column)

#     return moves

# print(matrix())
