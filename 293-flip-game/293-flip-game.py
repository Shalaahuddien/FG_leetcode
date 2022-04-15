class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        for i in range(len(currentState) - 1):
            if currentState[i : i + 2] == "++":
                nxt = list(currentState)
                nxt[i : i + 2] = list("--")
                res.append("".join(nxt))
        return res