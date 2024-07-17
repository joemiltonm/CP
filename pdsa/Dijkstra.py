dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
wlist = {}

for i in range(7):
    wlist[i] = []

for (u,v,w) in dedges:
    wlist[u].append((v,w))

print(wlist)

def dijkstr(wlist, start):

    infinity = 1+ len(wlist.keys()) * max([v for i in wlist.keys() for (u,v) in wlist[i]])

    visited, distance = {}, {}

    for i in range(len(wlist.keys())):
        visited[i] = False
        distance[i] = infinity
    
    distance[start] = 0
    
   
    for _ in wlist.keys():
        min_dist = min([distance[i] for i in wlist.keys() if not visited[i]])

        min_vertices = [i for i in wlist.keys() if not visited[i] and distance[i] == min_dist ]

        current_vertex = min_vertices[0]

        visited[current_vertex] = True

        for (u,v) in wlist[current_vertex]:
            if min_dist+v < distance[u]:
                distance[u] = min_dist + v
    
    return distance

print(dijkstr(wlist,0))