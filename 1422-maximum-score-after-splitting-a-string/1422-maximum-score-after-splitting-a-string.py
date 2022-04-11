class Solution:
    def maxScore(self, s: str) -> int:
        zeros = ones = 0
        ans = float("-inf")

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, zeros + ones)
        return ans - ones + (1 if s[-1] == "1" else 0)