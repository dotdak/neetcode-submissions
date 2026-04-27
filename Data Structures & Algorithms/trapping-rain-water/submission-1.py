class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        total = 0
        water_trapped = 0
        while L < R:
            if maxR >= maxL:
                L += 1
                water_trapped = min(maxL, maxR) - height[L]
                maxL = max(maxL, height[L])
            else:
                R -= 1
                water_trapped = min(maxL, maxR) - height[R]
                maxR = max(maxR, height[R])
            total += water_trapped if water_trapped > 0 else 0

        return total