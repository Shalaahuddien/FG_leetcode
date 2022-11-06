class Trie:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.children = defaultdict(Trie)
    
    def add(self, word):
        root = self
        for char in word:
            root = root.children[char]
        root.is_word = True
        root.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        res = []
        
        def dfs(row, col, node):
            if board[row][col] == '':
                return
            char = board[row][col]
            board[row][col] = ''
            
            child = node.children[char]
            if child.is_word:
                res.append(child.word)
                child.is_word = False
            
            if child.children:
                for drow, dcol in [[0,1],[1,0],[0,-1],[-1,0]]:
                    r, c = row+drow, col+dcol
                    if 0 <= r < rows and 0 <= c < cols and board[r][c] in child.children:
                        dfs(r, c, child)
			
			# the above dfs could have deleted some nodes, so recheck and prune if there is nothing left on this child
            if not child.children:
                del node.children[char]
            
            board[row][col] = char
            
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie.children:
                    dfs(row, col, trie)
        return res