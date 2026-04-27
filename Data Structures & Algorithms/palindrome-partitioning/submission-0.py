class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        ans = []
        def dfs(i, current_path):
            if i == len(s):
                ans.append(list(current_path))
                return
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if isPalin(substring):
                    current_path.append(substring)
                    dfs(j, current_path)
                    current_path.pop()
        dfs(0, [])
        return ans
