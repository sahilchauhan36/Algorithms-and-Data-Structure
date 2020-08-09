# This programs deals with the BFS Traversal of graph.
# Author : Sahil Chauhan

# edge data structure of graph
class edge:
  def __init__(self, y):
    self.y = y
    self.next_node = None

# graph data structure
class graph: 
  def __init__(self):
    self.nedges = 0
    self.nvertices = 0
    self.degree = dict()
    self.edges = dict()
    for i in range(0, 7):
      self.edges[i] = list()
      self.degree[i] = 0
  
  def insert_edge(self, x, y, directed):
    # create an edge
    x_y_edge = edge(y)
    x_y_edge.next_node = None

    # add edge to graph
    self.edges[x].append(x_y_edge)

    # Update vertices count 
    if self.degree[x] == 0:
      self.nvertices += 1
    
    # increment degree
    self.degree[x] += 1

    if not directed:
      # for undirected graph insert it for (y,x)
      self.insert_edge(y, x, True)
    else:
      self.nedges+=1
  
  def bfs_traversal(self):
    visited = list()
    print("BFS Order: ")
    
    # set visited for all nodes to false
    for i in range(0, self.nvertices+1):
      visited.append(False)
    
    queue = []
    queue.append(0) # add starting node to queue

    # iterate till the list is not empty
    while(len(queue) != 0):
      element = queue[0]

      queue.pop(0)
      visited[element] = True
      print(element)

      p = self.edges[element]
      
      for node in p:
        if visited[node.y] == False:
          queue.append(node.y)
    

# instatiation of graph
g = graph()

# insert edges in graph
g.insert_edge(1,2, False)
g.insert_edge(0,1, False)
g.insert_edge(1,3, False)
g.insert_edge(2,5, False)
g.insert_edge(1,6, False)

# bfs traversal
g.bfs_traversal()
