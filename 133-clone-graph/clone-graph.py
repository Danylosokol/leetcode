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
        if not node:
            return None
        adjacencyList = {}
        visited = set()
        queue = deque([node])
        root = None
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            if cur.val not in adjacencyList:
                adjacencyList[cur.val] = Node(cur.val, [])
                if not root:
                    root = adjacencyList[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in adjacencyList:
                    queue.append(neighbor)
                    adjacencyList[neighbor.val] = Node(neighbor.val, [])
                neighbor = adjacencyList[neighbor.val]
                adjacencyList[cur.val].neighbors.append(neighbor)
        return root
        
