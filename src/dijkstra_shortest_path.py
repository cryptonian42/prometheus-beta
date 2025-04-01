import heapq
from typing import Dict, List, Optional, Tuple

def dijkstra_shortest_path(graph: Dict[str, Dict[str, int]], start: str, end: str) -> Optional[Tuple[List[str], int]]:
    """
    Find the shortest path between start and end nodes in a weighted graph using Dijkstra's algorithm.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A dictionary representing the weighted graph. 
                                           Keys are nodes, values are dictionaries of neighboring nodes and their edge weights.
        start (str): The starting node.
        end (str): The destination node.
    
    Returns:
        Optional[Tuple[List[str], int]]: A tuple containing the shortest path (list of nodes) and total distance, 
                                         or None if no path exists.
    
    Raises:
        ValueError: If start or end nodes are not in the graph.
    """
    # Validate input nodes exist in the graph
    if start not in graph or end not in graph:
        raise ValueError("Start or end node not in graph")
    
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    # Priority queue to store nodes to visit (distance, node)
    pq = [(0, start)]
    
    # Track visited nodes
    visited = set()
    
    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # If we've reached the end node, reconstruct and return the path
        if current_node == end:
            path = []
            walk_node = current_node
            path_distance = 0
            while walk_node:
                path.append(walk_node)
                if predecessors[walk_node] is not None:
                    path_distance += graph[predecessors[walk_node]][walk_node]
                walk_node = predecessors[walk_node]
            return list(reversed(path)), path_distance
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node].items():
            # Calculate distance to neighbor through current node
            distance = current_distance + weight
            
            # If this path is shorter, update distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return None