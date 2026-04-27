class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        rank = {}
        for n in nums:
            parent[n] = n
            rank[n] = 0

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
        
        for num in parent:
            if num - 1 in parent:
                union(num - 1, num)
        
        counter = {}
        ans = 0
        for num in parent:
            root = find(num)
            if root != num:
                counter[root] = counter.get(root, 1) + 1
            ans = max(ans, counter.get(root, 1))
        return ans