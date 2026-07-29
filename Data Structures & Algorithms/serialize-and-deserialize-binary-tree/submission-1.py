# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        encoded = []
        frontier = [root]
        while frontier:
            new = []
            for node in frontier:
                if node is None:
                    encoded.append(".")
                    continue
                encoded.append(str(node.val))
                new.append(node.left)
                new.append(node.right)
            frontier = new
        return ",".join(encoded)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = data.split(",")
        frontier = [data[0]]
        head = TreeNode(int(data[0]))
        i, n = 1, len(data)
        pointers = [head]
        while pointers and i < n:
            new = []
            for node in pointers:
                if i < n and data[i] != ".":
                    node.left = TreeNode(int(data[i]))
                    new.append(node.left)
                i += 1
                if i < n and data[i] != ".":
                    node.right = TreeNode(int(data[i]))
                    new.append(node.right)
                i += 1
            pointers = new
        return head
