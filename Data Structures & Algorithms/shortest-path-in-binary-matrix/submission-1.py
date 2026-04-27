class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        moves = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
        
        visited = set()
        q = deque()
        q.append((0, 0, 1))
        while len(q) > 0:
            for _ in range(len(q)):
                r, c, path = q.popleft()
                if r == c == n - 1:
                    return path
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        q.append((nr, nc, path + 1))
                        visited.add((nr, nc))
        return -1
