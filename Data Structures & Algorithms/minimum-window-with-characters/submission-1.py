from copy import deepcopy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # l, r = 0, len(s) - 1
        ans = s
        t_counter = Counter(t)
        valid = False
        for i in range(len(s)):
            if s[i] in t_counter:
                # l = i
                counter = deepcopy(t_counter)
                for j in range(i, len(s)):
                    if s[j] in counter:
                        counter[s[j]] = counter.get(s[j]) - 1
                        if counter[s[j]] <= 0:
                            counter.pop(s[j])
                        if len(counter) == 0:
                            valid = True
                            if len(s[i:j+1]) < len(ans):
                                ans = s[i:j+1]
                            break
        return ans if valid else ""
