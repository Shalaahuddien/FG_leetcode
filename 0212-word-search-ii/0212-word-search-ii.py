'''
So, we are putting all the words in trie set to avoid any duplication in matching
- First Key thing for is, when we explore the leaf, we cut that leaf and never visit that again
- Second thing is, here, there is no global visited set like bfs.. since "order of traversal
matters", so we keep track of each different traversal by having different visited set for each call

'''
class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        # simple trie structure; nothing special here.
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.word = w

        # core of the solution
        def backtracking(node, loc, visited):
            i, j = loc
            if loc in visited: return
            letter = board[i][j]
            # this is required, as the current path is not a part of any prefix of the given words
            # so we can just stop searching in this direction
            if letter not in node.children: return
            prev = node
            node = node.children[letter]

            # most important: without this, I am getting TLE
            # we visited leaf and we are cutting this leaf and we will never see that again!
            if not node.children: del prev.children[letter]

            # if an entire word is matched, we can store it
            if node.word: self.ans.add(node.word)

            # searching in all the directions
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # going out of the board
                if i+dir[0] >= len(board) or j+dir[1] >= len(board[0]) or i+dir[0] < 0 or j+dir[1] < 0:
                    continue
                # we have different visited set for each call, it will have the previous path
                # if we change the path with the same start location, we will have different path
                backtracking(node, (i+dir[0], j+dir[1]), visited.union({(i,j)}))
        
        self.ans = set()

        # every cell position is a possible start location.
        for i in range(len(board)):
            for j in range(len(board[0])):
                # since we are passing trie, if that cell location is not a child of a root
                # we will just return the function and move to the different location
                backtracking(root, (i, j), set())
        return self.ans
