class Solution:
    def toHexspeak(self, num: str) -> str:
        x16 = hex(int(num))[2:]
        after = x16.replace("0", "O").replace("1", "I").upper()
        valid = {"A", "B", "C", "D", "E", "F", "I", "O"}
        if all(c in valid for c in set(after)):
            return "".join(after)
        return "ERROR"