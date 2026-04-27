class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        reach_pacific = set()
        reach_atlantic = set()
        def dfs(r, c, prev_h, visit):
            if not 0 <= r < m or not 0 <= c < n or heights[r][c] < prev_h or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in moves:
                dfs(r + dr, c + dc, heights[r][c], visit)
        
        for r in range(m):
            dfs(r, 0, heights[r][0], reach_pacific)
            dfs(r, n-1, heights[r][n-1], reach_atlantic)
        for c in range(n):
            dfs(0, c, heights[0][c], reach_pacific)
            dfs(m-1, c, heights[m-1][c], reach_atlantic)
        ans = []
        for r in range(m):
            for c in range(n):
                if (r, c) in reach_pacific and (r, c) in reach_atlantic:
                    ans.append([r, c])
        return ans