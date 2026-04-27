class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            counter = defaultdict(int)
            for j in range(len(board[0])):
                counter[board[i][j]] += 1
                if board[i][j] != '.' and counter[board[i][j]] > 1:
                    return False
        
        for j in range(len(board[0])):
            counter = defaultdict(int)
            for i in range(len(board)):
                counter[board[i][j]] += 1
                if board[i][j] != '.' and counter[board[i][j]] > 1:
                    return False

        for n in range(0, len(board), 3):
            for m in range(0, len(board[0]), 3):
                counter = defaultdict(int)
                for i in range(n, n+3):
                    for j in range(m, m+3):
                        counter[board[i][j]] += 1
                        if board[i][j] != '.' and counter[board[i][j]] > 1:
                            return False

        return True