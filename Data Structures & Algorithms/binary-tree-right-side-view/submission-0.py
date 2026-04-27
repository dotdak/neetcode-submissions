# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans

        levels = []
        queue = [root]

        currentLevel = 0
        while queue:
            levels.append([])
            for _ in range(len(queue)):
                node = queue.pop(0)
                levels[currentLevel].append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            currentLevel += 1

        for vals in levels:
            ans.append(vals[-1])

        return ans