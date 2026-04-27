class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for s in strs:
            c = "".join(sorted(s))
            counter.setdefault(c, []).append(s)
        ans = []
        for key in counter:
            ans.append(counter.get(key))

        return ans