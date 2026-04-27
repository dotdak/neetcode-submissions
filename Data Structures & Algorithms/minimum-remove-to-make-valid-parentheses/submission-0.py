class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = []
        for i in range(len(s)):
            c = s[i]
            ans.append(c)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    ans[i] = ""
            elif c == '(':
                stack.append(i)
        while stack:
            ans[stack.pop()] = ""

        return "".join(ans)
                