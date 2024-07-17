
import numpy as np
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]

size = 7

AdjMatrix = np.zeros(shape=(size,size,2))

for (i,j,k) in dedges:
    AdjMatrix[i][j][0] = 1
    AdjMatrix[i][j][1] = k

#print("matirx",AdjMatrix)

AdjList = {}

for i in range(size):
    AdjList[i] = []

for (i,j,k) in dedges:
    AdjList[i].append((j,k))

#print(AdjList)

# undirected graph. forming the DS

# dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]

# forming adjlist from the above. 

udlist = {}

all_edges = dedges + [(v,u,w) for (u,v,w) in dedges]

for i in range(7):
    udlist[i] = []

for (u,v,w) in all_edges:
    udlist[u].append((v,w))

print(udlist)

