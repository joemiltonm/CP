
class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, v):
        self.stack.append(v)
    
    def isEmpty(self):
        return self.stack == []
    
    def pop(self):
        v = None
        if not self.isEmpty():
            v = self.stack.pop()
        
        return v
    def __str__(self):
        return (str(self.stack))
        
    

AList ={0: [ 1,2 ], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}


def DFS(start, list):
    visited = {}
    parent = {}

    for i in list.keys():
        visited[i] = False
        parent[i] = -1
    
    st = stack()

    st.push(start)

    while (not st.isEmpty()):

        v = st.pop()

        if visited[v] == False:
            visited[v] = True
            for i in list[v]:
                if visited[i] == False:
                    parent[i] = v
                    st.push(i)
        print(st)
        
    return visited, parent


print(DFS(0,AList))
