# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p = head
        n = 1
        while p.next is not None:
            p = p.next
            n += 1
        tail = p
        k %= n
        if k == 0:
            return head

        p = head
        for _ in range(n - k - 1):
            p = p.next
        new_head = p.next
        p.next = None
        tail.next = head
        return new_head
