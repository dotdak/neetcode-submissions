class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and h < stack[-1][1]:
                prev_inx, prev_h = stack.pop()
                area = prev_h * (i - prev_inx)
                maxArea = max(maxArea, area)
                start = prev_inx
            stack.append((start, h))
            maxArea = max(maxArea, h)
        return maxArea