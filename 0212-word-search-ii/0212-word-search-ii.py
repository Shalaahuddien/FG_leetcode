class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board = {i+j*1j: c for i, row in enumerate(board) for j, c in enumerate(row)}
        res, trie = [], (Trie:=lambda: defaultdict(Trie))()
        any(reduce(dict.__getitem__, word, trie).__setitem__(None, word) for word in words)
        def dfs(z, parent):
            if not (c:=board.get(z)) in parent:
                return
            if (word:=(node:=parent[c]).pop(None, None)):
                res.append(word)
            board[z] = None
            any(dfs(z+1j**k, node) for k in range(4))
            board[z] = c
            if not node:
                parent.pop(c)
        any(dfs(z, trie) for z in board)
        return res