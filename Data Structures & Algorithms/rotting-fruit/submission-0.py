class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()
        fresh = 0
        minutes = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while fresh > 0 and len(q) > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            minutes += 1
        return minutes if fresh == 0 else -1