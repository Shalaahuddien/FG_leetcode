class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [len(s) + 1] * len(s)
        prev = next = -1
        for i in range(len(s)):
            if c == s[i]:
                prev = i
            if prev != -1:
                ans[i] = i - prev
        for j in range(len(s) - 1, -1, -1):
            if c == s[j]:
                next = j
            if next != -1:
                ans[j] = min(ans[j], next - j)
        return ans