class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = 0
    
    def addWord(self, word, weight):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr.children[c].weight = weight
            curr = curr.children[c]

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for idx, word in enumerate(words):
            length = len(word + "#")
            word = word + "#" + word

            for i in range(length):
                self.root.addWord(word[i:], idx)
        

    def f(self, pref: str, suff: str) -> int:
        curr = self.root

        for c in (suff + '#' + pref):
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        return curr.weight


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)