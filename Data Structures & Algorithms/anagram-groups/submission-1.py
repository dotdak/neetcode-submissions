class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                inx = ord(c) - ord('a')
                key[inx] += 1
            counter.setdefault(tuple(key), []).append(s)
        ans = []
        for key in counter:
            ans.append(counter.get(key))

        return ans