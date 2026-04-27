# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def find(node):
            nonlocal lca
            if node is None:
                return [False, False]

            
            foundPLeft, foundQLeft = find(node.left)
            foundPRight, foundQRight = find(node.right)
            
            foundP = foundPLeft or foundPRight or node == p
            foundQ = foundQLeft or foundQRight or node == q
            
            if foundP and foundQ and not lca:
                lca = node
            return [foundP, foundQ]

        find(root)
        return lca