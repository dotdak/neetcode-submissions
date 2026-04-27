class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        p = self.trie
        for c in word:
            p[c] = p.get(c, {})
            p = p[c]
        p['#'] = None

    def searchTrie(self, trie, word):
        for i in range(len(word)):
            if word[i] == '.':
                for c in trie:
                    if c == '#':
                        continue
                    elif self.searchTrie(trie.get(c, {}), word[i+1:]):
                        return True
                else:
                    return False
            elif trie.get(word[i], None) is None:
                return False
            trie = trie.get(word[i], {})
        return '#' in trie

    def search(self, word: str) -> bool:
        return self.searchTrie(self.trie, word)

