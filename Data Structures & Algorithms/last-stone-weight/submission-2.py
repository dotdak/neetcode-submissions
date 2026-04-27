import heapq
class Heap:
    def __init__(self):
        self.heap = None
    def heapify(self, arr):
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1 ) // 2
        while cur > 0:
            i = cur
            while i*2 < len(self.heap):
                if (i * 2 + 1) < len(self.heap) and self.heap[i] < self.heap[i*2 +1] and self.heap[i * 2] < self.heap[2 * i + 1]:
                    self.heap[i], self.heap[i*2 + 1] = self.heap[i*2 + 1], self.heap[i]
                    i = i * 2 + 1
                elif self.heap[i] < self.heap[i*2]:
                    self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                    i *= 2
                else:
                    break
            cur -= 1
        
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i//2] < self.heap[i]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i //= 2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        while i*2 < len(self.heap):
            if (i * 2 + 1) < len(self.heap) and self.heap[i] < self.heap[i*2 + 1] and self.heap[i*2] < self.heap[i*2+1]:
                self.heap[i*2 + 1], self.heap[i] = self.heap[i], self.heap[i*2 + 1]
                i = i * 2 + 1
            elif self.heap[i] < self.heap[i*2]:
                self.heap[i*2], self.heap[i] = self.heap[i], self.heap[i*2]
                i *= 2
            else:
                break
        return res
    def size(self):
        return len(self.heap) - 1

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = Heap()
        heap.heapify(stones)

        while heap.size() > 1:
            stone1, stone2 = heap.pop(), heap.pop()
            if stone1 - stone2 > 0:
                heap.push(stone1 - stone2)
        return 0 if heap.size() == 0 else heap.pop()
