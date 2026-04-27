from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        t_counter = Counter(t)
        for c in counter:
            if t_counter[c] != counter[c]:
                return False
            t_counter.pop(c)
        return len(t_counter) == 0