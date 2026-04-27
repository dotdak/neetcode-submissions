class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        amount = 0
        while L < R:
            amount = max(amount, min(heights[L], heights[R])*(R-L))
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return amount