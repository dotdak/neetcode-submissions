# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class ComparableListNode:
    def __init__(self, listNode):
        self.val = listNode.val
        self.next = listNode.next
        self.origin = listNode
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # frontier = sorted([listNode for listNode in lists], key = lambda node: node.val)
        frontier = [ComparableListNode(node) for node in lists]
        heapq.heapify(frontier)
        head = ListNode()
        p = head
        while frontier:
            minNode = heapq.heappop(frontier)
            p.next = minNode.origin
            if minNode.next is not None:
                heapq.heappush(frontier, ComparableListNode(minNode.next))
            p = p.next
        return head.next
            