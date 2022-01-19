from graph.graph import Graph, Vertex
import pytest

def test_add_node():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    assert g.size() == 2

def test_get_nodes():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    list_vertices = g.get_nodes()
    assert a in list_vertices
    assert b in list_vertices

def test_get_nodes_empty():
    g = Graph()
    assert g.get_nodes() == []

def test_size_empty():
    g = Graph()
    assert g.size() == 0

def test_add_edge_no_weight():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    c = g.add_node('C')
    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(b,a)
    c.add_edge(c,a)
    