


def DFSinit(list):
    visited = {}
    parent = {}
    for i in list.keys():
        visited[i] = False
        parent[i] = -1
    return visited, parent

def DFSr(list, visited, parent, start):

    visited[start] = True

    for i in list[start]:
        if visited[i] == False:
            parent[i] = start
            visited, parent = DFSr(list, visited, parent, i)
    
    return visited, parent

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

v,p = DFSinit(AList)

print(v,p)

print(DFSr(AList, v, p, 0))

