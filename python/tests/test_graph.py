from graph.graph import Graph, Vertex
import pytest

def test_add_node():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    assert g.size() == 2

@pytest.mark.skip()
def test_get_nodes():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    list_vertices = g.get_nodes()
    assert a in list_vertices
    assert b in list_vertices

@pytest.mark.skip()
def test_get_nodes_empty():
    g = Graph()
    assert g.get_nodes() == []

def test_size_empty():
    g = Graph()
    assert g.size() == 0