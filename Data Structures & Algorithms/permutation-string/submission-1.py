class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1Counter = Counter(s1)
        for i in range(len(s2) - window + 1):
            s2Counter = Counter(s2[i:i+window]) 
            for key in s2Counter:
                if key not in s1Counter or s1Counter[key] != s2Counter[key]:
                    break
            else:
                return True
        
        return False
