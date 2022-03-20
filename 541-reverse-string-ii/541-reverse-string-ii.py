class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = list(s)
        for i in range(0, len(ss), 2 * k):
            ss[i : i + k] = ss[i : i + k][::-1]
        return "".join(ss)