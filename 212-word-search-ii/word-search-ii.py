class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        result = set()

        def dfs(r, c, word, node):
            if(
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or board[r][c] not in node.children 
            ):
                return
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.word:
                result.add(word)

            dfs(r + 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c - 1, word, node)

            visited.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, "", root)
        
        return list(result)
        