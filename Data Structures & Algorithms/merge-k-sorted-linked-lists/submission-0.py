# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        frontier = sorted([listNode for listNode in lists], key = lambda node: node.val)
        head = ListNode()
        p = head
        while frontier:
            minNode = frontier.pop(0)
            p.next = minNode
            if minNode.next is not None:
                frontier.append(minNode.next)
                frontier = sorted(frontier, key = lambda node: node.val)
            p = p.next
        return head.next
            