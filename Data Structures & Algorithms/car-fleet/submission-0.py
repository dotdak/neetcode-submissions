class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in fleets:
            stack.append((target-p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
