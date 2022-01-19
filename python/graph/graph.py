from collections import deque

class Graph():
    def __init__(self):
        self.vertices = {}

    def size(self):
        return len(self.vertices)

    def add_node(self,val):
        self.vertices[Vertex(val)] = deque()

class Vertex():
    def __init__(self,value):
        self.value = value