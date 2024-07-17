
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] 


def MATinit(v, e):
    matrix = []
    visited = {}
    for i in range(len(v)):
        visited[i] = False

    for i in range(len(v)):
        row = []
        for j in range(len(v)): 
            row.append(0)

        matrix.append(row)
    
    for (x,y) in e:
        matrix[x][y] = 1
    
    return matrix, visited

def DFSr(matrix, start, visited):
    print("in recur",visited)
    visited[start] = True

    for neighbour in range(len(matrix[start])):
        if matrix[start][neighbour] == 1:
            if visited[neighbour] == False:
                visited = DFSr(matrix, neighbour, visited )

    return visited


matrix, visited = MATinit(V,E)
print(visited)
print(matrix)
print(DFSr(matrix, 0, visited))










