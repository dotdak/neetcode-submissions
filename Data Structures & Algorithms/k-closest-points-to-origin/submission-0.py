import math
import heapq
class Node:
    def __init__(self, distance, point):
        self.distance = distance
        self.point = point
    def __lt__(self, other):
        return self.distance < other.distance
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for [x, y] in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(distances, Node(distance, [x, y]))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(distances).point)
        return ans