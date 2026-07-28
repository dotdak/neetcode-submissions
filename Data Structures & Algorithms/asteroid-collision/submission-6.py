class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and -ast > stack[-1]:
                stack.pop()
            if stack and stack[-1] > 0 and -ast == stack[-1]:
                stack.pop()
                ast = 0
            if (not stack or stack[-1] < 0) and ast < 0 or ast > 0:
                stack.append(ast)
        return stack
                