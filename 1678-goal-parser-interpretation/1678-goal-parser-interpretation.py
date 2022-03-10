class Solution:
    def interpret(self, CMD: str) -> str:
        return CMD.replace("()", "o").replace("(al)", "al")
