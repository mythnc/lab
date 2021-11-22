class Trie:

    def __init__(self):
        self.words = set()
        self.prefixs = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        n = len(word)
        while n > 0:
            self.prefixs.add(word[:n])
            n -= 1

    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixs
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
