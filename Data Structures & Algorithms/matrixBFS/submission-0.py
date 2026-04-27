class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()
        q = deque()
        q.append((0, 0))
        path = 0
        while len(q) > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == m - 1 and c == n - 1:
                    return path
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            path += 1
        return -1