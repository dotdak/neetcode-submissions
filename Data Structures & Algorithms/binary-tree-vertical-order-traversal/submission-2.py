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
        min_index = max_index = 0
        while queue:
            node, index = queue.popleft()
            min_index = min(min_index, index)
            max_index = max(max_index, index)
            if node:
                maps.setdefault(index, []).append(node.val)
                queue.append((node.left, index - 1))
                queue.append((node.right, index + 1))
        ans = []
        for i in range(min_index, max_index + 1):
            if maps.get(i) is not None:
                ans.append(maps[i])
        return ans
