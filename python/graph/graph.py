from collections import deque

class Graph():
    def __init__(self):
        self.vertices = {}

    def size(self):
        return len(self.vertices)

    def add_node(self,val):
        vertex_to_add = Vertex(val)
        self.vertices[vertex_to_add] = deque()
        return vertex_to_add

    def get_nodes(self):
        return list(self.vertices.keys())

class Vertex():
    def __init__(self,value):
        self.value = value