import unittest
from abc import ABC

class GraphInterface(ABC):

    def add_node(self, node):
        return NotImplemented

    def node_count(self):
        return NotImplemented

    def add_edge(self, nd1, nd2):
        return NotImplemented

    def edge_count(self):
        return NotImplemented

    def edge_exists(self, nd1, nd2):
        return NotImplemented


class Graph(GraphInterface):

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        if node not in self.nodes :
            self.nodes.append(node)

    def node_count(self):
        return len(self.nodes)

    def add_edge(self, nd1, nd2):
        if nd1 != nd2 and nd1 in self.nodes and nd2 in self.nodes :
            self.edges.append(nd1 + ':' + nd2)

    def edge_count(self):
        return len(self.edges)

    def edge_exists(self, nd1, nd2):
        if (((nd1 + ':' + nd2) in self.edges) or ((nd2 + ':' + nd1) in self.edges)) :
            return True
        else :
            return False


class TestGraph(unittest.TestCase):

    def test_add_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        self.assertEqual(g.node_count(), 2)

    def test_add_edge(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n2")
        self.assertEqual(g.edge_count(), 1)

    def test_add_same_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n1")
        self.assertEqual(g.node_count(), 1)

    def test_add_edge_same_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n1")
        self.assertEqual(g.edge_count(), 0)

    def test_add_edge_on_missing_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n2", "n3")
        self.assertEqual(g.edge_count(), 0)

    def test_edge_exists_true(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n2")
        self.assertTrue(g.edge_exists("n1", "n2"))

    def test_edge_exists_true_wrong_order(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n2")
        self.assertTrue(g.edge_exists("n2", "n1"))

    def test_edge_exists_true(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_node("n3")
        g.add_edge("n1", "n2")
        self.assertFalse(g.edge_exists("n1", "n3"))

if __name__ == '__main__':
    unittest.main()