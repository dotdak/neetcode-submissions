# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class ComparableListNode:
    def __init__(self, listNode):
        self.node = listNode
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        frontier = [ComparableListNode(node) for node in lists]
        heapq.heapify(frontier)
        head = ListNode()
        p = head
        while frontier:
            minNode = heapq.heappop(frontier)
            p.next = minNode.node
            if minNode.node.next is not None:
                heapq.heappush(frontier, ComparableListNode(minNode.node.next))
            p = p.next
        return head.next
            