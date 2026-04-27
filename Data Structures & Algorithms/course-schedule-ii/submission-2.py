class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visit, cycle = set(), set()
        ans = []
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            visit.add(node)
            ans.append(node)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return ans

