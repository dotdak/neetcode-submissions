class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        s = '#' + '#'.join(s) + '#'

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l] != '#':
                    count += 1
                l -= 1
                r += 1
            
        return count

        
        