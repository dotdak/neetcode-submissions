class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            graph.setdefault(a, []).append(b)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if graph.get(course, None) is None:
                return True
            visited.add(course)
            for neighbor in graph.get(course, []):
                if not dfs(neighbor):
                    return False
            visited.discard(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True