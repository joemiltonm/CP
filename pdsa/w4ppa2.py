# Helper functions
from collections import deque
class myQueue:
  def __init__(self):
    self.Q = deque()
  
  def deQueue(self):
    return self.Q.popleft()

  def enQueue(self, x):
    return self.Q.append(x)

  def isEmpty(self):
    return False if self.Q else True

# Function  
def findAllPaths(vertices, gList, source , destination):
  allPaths=[]
  path=[]
  visited = {v:False for v in vertices}
  findAllPathsRecursive(vertices, gList, source, destination, visited, path, allPaths)
  return allPaths

# Function that will be called recursively to find path from original source to destination, that passes through vertex 'src'.
# If a path is found add it o allPaths.  
def findAllPathsRecursive(vertices, gList, src, dest, visited, path, allPaths):
  visited[src] = True
  path.append(src)
  print("path", path)

  if (src == dest):
    allPaths.append(path.copy())
    print("all paths", allPaths)

  for e in gList[src]:
    if not visited[e]:
      findAllPathsRecursive(vertices, gList, e, dest, visited, path, allPaths)

  # If no path exist passing through this vertex remove it from path.
  # Mark it unvisited, this vertex could be part of some other path.
  print("visited", visited)
  path.pop()
  visited[src]=False
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

# v = [item for item in input().split(" ")]
# Alist = {}
# for i in v:
#   Alist[i] = [item for item in input().split(" ") if item != '']
# source = input()
# dest = input()

v = [1,2,3,4,5,6,7,8]
Alist = {1:[3,4], 2:[3], 3:[6], 4:[6,7], 5:[4,6], 6:[2], 7:[5]}
source = 1
dest = 2

print(ArrangeResult(findAllPaths(v, Alist, source, dest)))