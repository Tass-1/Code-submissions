from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. Build the graph using an adjacency list
        graph = defaultdict(list)
        for (num, denom), weight in zip(equations, values):
            graph[num].append((denom, weight))
            graph[denom].append((num, 1.0 / weight))
            
        # 2. Define the recursive DFS helper function
        def dfs(curr_node, target_node, visited):
            # Base Case 1: If either node doesn't exist in our equations, it's undefined
            if curr_node not in graph or target_node not in graph:
                return -1.0
                
            # Base Case 2: We reached the target node! 
            if curr_node == target_node:
                return 1.0
                
            # Mark the current node as visited so we don't walk backwards in a loop
            visited.add(curr_node)
            
            # Look at every neighbor connected to our current node
            for neighbor, weight in graph[curr_node]:
                if neighbor not in visited:
                    # Recursively keep walking from the neighbor towards the target
                    path_weight = dfs(neighbor, target_node, visited)
                    
                    # If the search did NOT hit a dead end...
                    if path_weight != -1.0:
                        # Multiply the weight of the step we just took by the weight of the rest of the path
                        return weight * path_weight
                        
            # If we check all neighbors and none lead to the target, it's a dead end
            return -1.0
            
        # 3. Run the DFS for every query and collect the results
        results = []
        for start, target in queries:
            # Pass a brand new, empty set() for every single query 
            # so the "visited" tracker resets each time
            ans = dfs(start, target, set())
            results.append(ans)
            
        return results