E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]

def create_matrix(a,b):
    x = []
    for i in range(0,a):
        m = []
        for j in range(0,b):
            m.append(0)

        x.append(m)
    
    return x

mat = create_matrix(5,5)

print(mat)

for (i,j) in E:
    mat[i][j] = 1

print(mat)
