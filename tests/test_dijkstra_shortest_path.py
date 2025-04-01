import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    """Test a simple graph with a clear shortest path."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4

def test_single_node_path():
    """Test path from a node to itself."""
    graph = {
        'A': {},
        'B': {}
    }
    graph['A']['A'] = 0
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_no_path_exists():
    """Test when no path exists between nodes."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    assert dijkstra_shortest_path(graph, 'A', 'C') is None

def test_complex_graph_shortest_path():
    """Test a more complex graph with multiple possible paths."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4

def test_invalid_start_node():
    """Test raising an error for an invalid start node."""
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start or end node not in graph"):
        dijkstra_shortest_path(graph, 'C', 'A')

def test_invalid_end_node():
    """Test raising an error for an invalid end node."""
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start or end node not in graph"):
        dijkstra_shortest_path(graph, 'A', 'C')

def test_disconnected_graph():
    """Test a graph where nodes are not connected."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    assert dijkstra_shortest_path(graph, 'A', 'C') is None