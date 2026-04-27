import copy
class Trie:
    def __init__(self):
        self.head = {}
    
    def addWord(self, word):
        p = self.head
        for c in word:
            p.setdefault(c, {})
            p = p[c]
        p['#'] = True
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        ans = []
        def traverse(s, node, currentAns):
            if s == "":
                ans.append(" ".join(currentAns))
                return
            
            for i in range(len(s)):
                c = s[i]
                node = node.get(c)
                if node is None:
                    return
                if '#' in node:
                    currentAnsCloned = list(currentAns)
                    currentAnsCloned.append(s[:i+1])
                    traverse(s[i+1:], trie.head, currentAnsCloned)
        
        traverse(s, trie.head, [])
        return ans
