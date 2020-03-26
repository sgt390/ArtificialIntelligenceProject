import networkx as nx
import numpy as np


def matrix_to_edges(m: np.array):
    height, width = m.shape
    nodes = range(m.size)
    edges = set()
    for (x, y), el in np.ndenumerate(m):
        u = x*width + y
        if el == 0:
            v = (x-1)*width + y
        elif el == 1:
            v = u + 1
        elif el == 2:
            v = (x+1)*width + y
        elif el == 3:
            v = u - 1
        else:
            continue
        edges.add((u, v))
    return nodes, edges


def matrix_to_graph(m: np.array):
    g = nx.Graph()
    nodes, edges = matrix_to_edges(m)
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    return g


def connected_components(m: np.array):
    g = matrix_to_graph(m)
    return nx.number_connected_components(g)
