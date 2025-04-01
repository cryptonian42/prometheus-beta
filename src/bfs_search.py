from collections import deque
from typing import List, Dict, Any, Optional, Callable

def breadth_first_search(graph: Dict[Any, List[Any]], 
                          start: Any, 
                          goal: Optional[Any] = None, 
                          visit_fn: Optional[Callable[[Any], bool]] = None) -> List[Any]:
    """
    Perform Breadth-First Search on a graph.

    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph
        start (Any): Starting node for the search
        goal (Optional[Any], optional): Goal node to find. Defaults to None.
        visit_fn (Optional[Callable[[Any], bool]], optional): Custom visit function. Defaults to None.

    Returns:
        List[Any]: List of nodes visited during the search

    Raises:
        ValueError: If the start node is not in the graph
        TypeError: If the graph is not a valid dictionary
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")

    # Initialize data structures
    visited = set()
    queue = deque([start])
    traversal_order = []

    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Skip if already visited
        if current in visited:
            continue
        
        # Mark as visited
        visited.add(current)
        traversal_order.append(current)

        # Check custom visit function if provided
        if visit_fn and visit_fn(current):
            break

        # Check if goal is reached and stop the search
        if current == goal:
            break

        # Add unvisited neighbors to queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)

        # If goal is not None and goal is in queue, break to stop further exploration
        if goal is not None and goal in queue:
            break

    return traversal_order