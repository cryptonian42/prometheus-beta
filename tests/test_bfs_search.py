import pytest
from src.bfs_search import breadth_first_search

def test_basic_bfs():
    """Test basic BFS traversal"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    result = breadth_first_search(graph, start='A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_bfs_with_goal():
    """Test BFS with a specific goal node"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    result = breadth_first_search(graph, start='A', goal='F')
    assert result == ['A', 'B', 'C', 'F']

def test_bfs_with_visit_fn():
    """Test BFS with a custom visit function"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    def stop_at_d(node):
        return node == 'D'
    
    result = breadth_first_search(graph, start='A', visit_fn=stop_at_d)
    assert result == ['A', 'B', 'C', 'D']

def test_bfs_disconnected_graph():
    """Test BFS on a graph with disconnected components"""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    result = breadth_first_search(graph, start='A')
    assert result == ['A', 'B']

def test_bfs_single_node_graph():
    """Test BFS on a graph with a single node"""
    graph = {
        'A': []
    }
    
    result = breadth_first_search(graph, start='A')
    assert result == ['A']

def test_invalid_graph():
    """Test handling of invalid graph input"""
    with pytest.raises(TypeError):
        breadth_first_search([], start='A')

def test_invalid_start_node():
    """Test handling of non-existent start node"""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    with pytest.raises(ValueError):
        breadth_first_search(graph, start='C')