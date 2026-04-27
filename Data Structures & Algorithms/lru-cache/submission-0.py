class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
        else:
            if len(self.cache) >= self.cap:
                del self.cache[self.tail.key]
                self._remove(self.tail)
            node = Node(key, value, None, None)
            self.cache[key] = node
        self._add_to_front(node)

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None

    def _add_to_front(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
