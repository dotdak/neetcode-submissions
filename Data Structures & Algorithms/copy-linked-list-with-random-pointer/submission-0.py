"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {}
        p = head

        new_head = Node(0)
        new_p = new_head
        while p is not None:
            new_node = Node(p.val)
            copied[p] = new_node
            new_p.next = new_node
            new_p = new_p.next
            p = p.next
        
        p = head
        while p is not None:
            new_node = copied[p]
            new_node.random = copied[p.random] if p.random is not None else None
            p = p.next

        return new_head.next
