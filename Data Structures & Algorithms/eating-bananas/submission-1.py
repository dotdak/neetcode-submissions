class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            speed = (low + high) // 2
            actual_time = sum([math.ceil(p/speed) for p in piles])
            
            if actual_time <= h:
                res = speed
                high = speed - 1
            else:
                low = speed + 1

        return res