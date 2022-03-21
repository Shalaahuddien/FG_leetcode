class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_c, sec_last_c = -1, -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and last_c == -1:
                last_c = i
            if last_c != -1 and s[i] == " ":
                sec_last_c = i
                return last_c - sec_last_c
        return last_c + 1
