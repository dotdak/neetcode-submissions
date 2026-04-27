class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1Key = [0] * 26
        for c in s1:
            s1Key[ord(c) - ord('a')] += 1
        s1Key = tuple(s1Key)
        for i in range(len(s2) - window + 1):
            s2Key = [0] * 26
            for c in s2[i:i+window]:
                s2Key[ord(c) - ord('a')] += 1
            if tuple(s2Key) == s1Key:
                return True
        
        return False
