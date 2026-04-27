class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, None, None)
        self.cache = {}
        self.head.next, self.tail.prev = self.tail, self.head

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
                del self.cache[self.tail.prev.key]
                self._remove(self.tail.prev)
            node = Node(key, value, None, None)
            self.cache[key] = node
        self._add_to_front(node)

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_to_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        # old_next = self.head.next
        # node.prev, node.next = self.head, old_next
        # self.head.next = node
        # old_next.prev = node