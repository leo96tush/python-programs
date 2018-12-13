from collections import defaultdict
class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
    def __str__(self):
        return(self.id) + 
class Graph:
    def __init__(self,vertices):
        self.vertices = defaultdict(list)
    def add_edge(self,u,v):

