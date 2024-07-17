class myqueue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def is_empty(self):
        return self.queue == []

    def dequeue(self):
        v = 0
        if not self.is_empty():
            v = self.queue[0]
            self.queue.pop(0)
            return v
    def __str__(self):
        return self(str(self.queue))


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

def BFS(starting_vertex, list):

    visited = {}
    parent = {}

    for i in list.keys():
        visited[i] = 0
        parent[i] = 0

    queue = myqueue()
    queue.enqueue(starting_vertex)

    visited[starting_vertex] = 1
    parent[starting_vertex] = -1

    while not queue.is_empty():
        v = queue.dequeue()

        for i in list[v]:
            if visited[i] == 0:
                queue.enqueue(i)
                visited[i] = 1
                parent[i] = v

    return visited, parent

print(BFS(0, AList))