class Solution:
    def interpret(self, CMD: str) -> str:
        stk = []
        i = 0
        while i < len(CMD):
            if CMD[i] in "G(":
                stk.append(CMD[i])
            elif CMD[i] == "a":
                stk.pop()
                stk.append("al")
                i += 1
            elif CMD[i] == ")":
                if stk[-1] == "(":
                    stk.pop()
                    stk.append("o")
            i += 1
        return "".join(stk)