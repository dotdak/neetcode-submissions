class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        def find(n):
            while n != nodes[n]:
                nodes[n] = nodes[nodes[n]]
                n = nodes[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                nodes[p2] = p1
            elif rank[p2] > rank[p1]:
                nodes[p1] = p2
            else:
                nodes[p2] = p1
                rank[p1] += 1
        
        for n1,n2 in edges:
            union(n1,n2)

        ans = 0
        visited = set()
        for n in nodes:
            root = find(n)
            if root not in visited:
                ans += 1
                visited.add(root)

        return ans
