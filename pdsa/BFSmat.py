V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] 

Amat = []

for i in range(len(V)):
    row = []
    for j in range(len(V)):
        row.append(0)
    Amat.append(row)

for (i,j) in E:
    Amat[i][j] = 1

class queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, v):
        self.queue.append(v)

    def is_empty(self):
        return self.queue == []
    
    def dequeue(self):
        v = 0
        if not self.is_empty():
            v = self.queue[0]
            self.queue.pop(0)
        
        return v

    def __str__(self):
        return str(self.queue)

print(Amat)

def BFS(start, matrix):
    visited = {}

    for i in range(len(V)):
        visited[i] = False

    q = queue()

    q.enqueue(start)
    visited[start] = True

    while (not q.is_empty()):
        i = q.dequeue()

        for j in range(len(V)):
            if matrix[i][j] == 1:
                visited[j] = True
                q.enqueue(j)

    return visited


print(BFS(0, Amat))