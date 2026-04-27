class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for k, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, inx = stack.pop()
                ans[inx] = k - inx
            stack.append((temp, k))
        return ans