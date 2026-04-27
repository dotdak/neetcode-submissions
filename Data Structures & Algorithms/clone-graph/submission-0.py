"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        node_map = {}
        node_map[node] = Node(node.val)

        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                node_map[n].neighbors.append(node_map[neighbor])
        
        return node_map[node]