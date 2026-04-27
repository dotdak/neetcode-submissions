class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        indegree = [0] * numCourses 
        for i in range(numCourses):
            for node in graph[i]:
                indegree[node] += 1
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        ans = []
        while queue:
            top = queue.popleft()
            ans.append(top)
            for nei in graph[top]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return ans if len(ans) == numCourses else []

