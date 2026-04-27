class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        p = self.trie
        for s in word:
            p[s] = p.get(s, {})
            p = p[s]
        p['#'] = None

    def search(self, word: str) -> bool:
        p = self.trie
        for s in word:
            p = p.get(s, None)
            if p is None:
                return False
        return '#' in p

    def startsWith(self, prefix: str) -> bool:
        p = self.trie
        for s in prefix:
            p = p.get(s, None)
            if p is None:
                return False
        return True
        