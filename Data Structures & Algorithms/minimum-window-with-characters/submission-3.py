from copy import deepcopy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = s
        t_counter = Counter(t)
        valid = False
        s_counter = {}
        have = l = 0
        for r in range(len(s)):
            c = s[r]
            s_counter[c] = 1 + s_counter.get(c, 0)
            if c in t_counter and s_counter[c] == t_counter[c]:
                have += 1
            while have == len(t_counter):
                valid = True
                if r -l + 1 < len(ans):
                    ans = s[l:r+1]
                s_counter[s[l]] -= 1
                if s[l] in t_counter and s_counter[s[l]] < t_counter[s[l]]:
                    have -= 1
                l += 1
        
        return ans if valid else ""
