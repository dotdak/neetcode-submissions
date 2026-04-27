class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = Node(None)
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        node = self.head.next
        for i in range(index):
            if node is None:
                return -1
            node = node.next
        return node.val if node is not None else -1

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)

    def insertTail(self, val: int) -> None:
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(val)
        print(self.getValues())

    def remove(self, index: int) -> bool:
        node = self.head
        for i in range(index):
            if node is None:
                return False
            node = node.next
        if node is not None and node.next is not None:
            node.next = node.next.next
            return True
        return False  

    def getValues(self) -> List[int]:
        node = self.head.next
        values = []
        while node is not None:
            values.append(node.val)
            node = node.next
        return values