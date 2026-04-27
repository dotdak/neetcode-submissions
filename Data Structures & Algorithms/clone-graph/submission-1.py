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
        
        node_map = {}
        def dfs(node):
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val)
            node_map[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        # while q:
        #     n = q.popleft()
        #     for neighbor in n.neighbors:
        #         if neighbor not in node_map:
        #             node_map[neighbor] = Node(neighbor.val)
        #             q.append(neighbor)
        #         node_map[n].neighbors.append(node_map[neighbor])
        
        return dfs(node)