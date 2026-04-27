class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        newNode = Node(value, self.tail, self.tail.prev)
        self.tail.prev.next, self.tail.prev = newNode, newNode
        self.size += 1

    def appendleft(self, value: int) -> None:
        newNode = Node(value, self.head.next, self.head)
        self.head.next.prev, self.head.next = newNode, newNode
        self.size +=1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        value = self.tail.prev.val
        pivot = self.tail.prev.prev
        pivot.next, self.tail.prev = self.tail, pivot 
        self.size -= 1
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.next.val
        pivot = self.head.next.next
        pivot.prev, self.head.next = self.head, pivot
        self.size -= 1
        return value
