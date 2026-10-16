"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        seen = {}
        def fun(r):
            if not r:
                return
            t = Node(r.val)
            seen[r] = t
            for n in r.neighbors:
                if n in seen:
                    t.neighbors.append(seen[n])
                    continue
                a = fun(n)
                t.neighbors.append(a)
            return t
        
        return fun(node) 