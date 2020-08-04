# This programs deals with the basic implementation of graph.
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
    for i in range(0, 3):
      self.edges[i] = list()
      self.degree[i] = 0
  
  def insert_edge(self, x, y, directed):
    # create an edge
    x_y_edge = edge(y)
    x_y_edge.next_node = None

    # add edge to graph
    self.edges[x].append(x_y_edge)

    # increment degree
    self.degree[x] += 1

    if not directed:
      # for undirected graph insert it for (y,x)
      self.insert_edge(y, x, True)
    else:
      self.nedges+=1


# instatiation of graph
g = graph()

# insert edges in graph
g.insert_edge(1,2, False)
g.insert_edge(0,1, False)

# print graph
for i in range(0,3):
  print("Node : ", i)
  p = g.edges[i]
  for i in p:
    print(i.y)
