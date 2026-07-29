# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        curr = 0
        visited = set()
        def dfs(curr):
            visited.add(curr)
            for i in range(n):
                if curr != i and i not in visited and knows(curr, i):
                    return dfs(i)
            else:
                return curr
            return -1
        candidate = dfs(0)
        if candidate == -1:
            return -1

        for i in range(n):
            if not knows(i, candidate) or candidate != i and knows(candidate, i):
                return -1
        else:
            return candidate