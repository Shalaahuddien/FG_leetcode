class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words = [word, word[::-1]]
        n = len(word)
        for B in board, zip(*board):
            for row in B:
                q = "".join(row).split("#")
                for w in words:
                    for s in q:
                        if len(s) == n and all(ss in (" ", ww) for ss, ww in zip(s, w)):
                            return True
        return False