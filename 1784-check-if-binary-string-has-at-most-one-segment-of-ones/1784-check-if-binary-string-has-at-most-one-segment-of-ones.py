class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        all_one = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0" and all_one:
                return False
            if s[i] == "1":
                all_one = True
        return True