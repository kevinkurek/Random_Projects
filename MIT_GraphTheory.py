# MIT Graph Theory


#%%
# Node Class
class Node(object):

  def __init__(self,name):
    self.name = name
  def getName(self):
    return self.name
  def __str__(self):
    return self.name


# Edge Class

class Edge(object):

  def __init__(self,src,dest):
    self.src = src
    self.dest = dest
  
  def getSource(self):
    return self.src
  
  def getDestination(self):
    return self.dest
  
  def __str__(self):
    return self.src.getName() + "->" + self.dest.getName()

# Digraph Class

class Digraph(object):

  def __init__(self):
    self.edges = {}

  def addNode(self,node):
    if node in self.edges:
      raise ValueError('Duplicate Node')
    else:
      self.edges[node] = []
  
  def addEdge(self,edge):
    src = edge.getSource()
    dest = edge.getDestination()
    if not (src in self.edges and dest in self.edges):
      raise ValueError('Node not in graph')
    self.edges[src].append(dest)

  def childrenOf(self,node):
    return self.edges[node]

  def hasNode(self,node):
    return node in self.edges

  def getNode(self,name):
    for n in self.edges:
      if n.getName() == name:
        return n
    raise NameError(name)
  
  def __str__(self):
    result = ''
    for src in self.edges:
      for dest in self.edges[src]:
        result = result + src.getName() + '->' + dest.getName() + '\n'
    return result[:-1]


# Graph Class

class Graph(Digraph):
  def addEdge(self, edge):
    Digraph.addEdge(self,edge)
    rev = Edge(edge.getDestination(),edge.getSource())
    Digraph.addEdge(self,rev)


# Function Build City Graphs (Digraph & Graph)
def buildCityGraph(graphType):
  g = graphType()
  for name in ('Reno', 'Carson City', 'Tahoe', 'Sparks'):
    g.addNode(Node(name))

  g.addEdge(Edge(g.getNode('Reno'), g.getNode('Carson City')))
  g.addEdge(Edge(g.getNode('Tahoe'), g.getNode('Carson City')))

  return g

print('Digraph:\n',buildCityGraph(Digraph))

print('Graph:\n',buildCityGraph(Graph))