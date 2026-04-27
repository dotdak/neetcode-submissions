class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        direction = [(1,0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visit):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != 'O' or (r, c) in visit:
                return True
            
            visit.add((r,c))
            res = True
            for dr, dc in direction:
                if not dfs(r + dr, c + dc, visit):
                    res = False
            return res

        safe = set()
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m-1 or c == 0 or c == n-1) and board[r][c] == 'O':
                    dfs(r, c, safe)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'