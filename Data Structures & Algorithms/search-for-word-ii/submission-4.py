class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        move = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def findAt(i, j, word):
            if (
                i not in range(len(board))
                or j not in range(len(board[0]))
                or (i, j) in visited
                or board[i][j] != word[0]
            ): return False
            elif len(word) == 1 and board[i][j] == word: return True

            print('Find word: ', word, ' at: ', i, j, '. Visited: ', visited)
            visited.add((i, j))
            for di, dj in move:
                if findAt(i + di, j + dj, word[1:]):
                    return True
            visited.discard((i, j))
            return False

        def findAll(word):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        visited.clear()
                        print('Start finding word: ', word, ' at: ', i, j)
                        if findAt(i, j, word):
                            return word
            return None

        ans = []
        for word in words:
            if findAll(word):
                ans.append(word)
        return ans
# a b c
# a e d
# a f g
        
                        