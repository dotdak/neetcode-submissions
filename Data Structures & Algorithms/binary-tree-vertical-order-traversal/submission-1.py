# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        maps = {}
        queue = collections.deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            if node:
                maps.setdefault(index, []).append(node.val)
                queue.append((node.left, index - 1))
                queue.append((node.right, index + 1))
        ans = []
        indexes = sorted(maps)
        for i in indexes:
            ans.append(maps[i])
        return ans
