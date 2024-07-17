class MakeUnionFind:
    def __init__(self):
        self.components = {}
        self.size = 0
    def make_union_find(self,vertices):
        self.size = vertices
        for vertex in range(vertices):
            self.components[vertex] = vertex

    def find(self,vertex):
        return self.components[vertex]
    
    def union(self,u,v):
        c_old = self.components[u]
        c_new = self.components[v]
        for k in range(self.size):
            if self.components[k] == c_old:
                self.components[k] = c_new


x = MakeUnionFind()
x.make_union_find(5)
print(x.components,"\nsize", x.size)
print(x.find(3))
x.union(2,3)
print(x.components)
x.union(1,2)
print(x.components)
x.union(3,4)
print(x.components)
