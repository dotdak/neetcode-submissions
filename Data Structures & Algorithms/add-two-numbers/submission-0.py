# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        p1, p2, p3 = l1, l2, l3
        acc = 0
        while p1 and p2:
            new_val = (p1.val + p2.val + acc) % 10
            acc = (p1.val + p2.val + acc) // 10
            p3.next = ListNode(new_val)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
            
        
        if p2 and not p1:
            p1, p2 = p2, p1

        while p1:
            new_val = (p1.val + acc) % 10
            acc = (p1.val + acc) // 10
            p3.next = ListNode(new_val)
            p3 = p3.next
            p1 = p1.next

        if acc:
            p3.next = ListNode(1)
        
        return l3.next
