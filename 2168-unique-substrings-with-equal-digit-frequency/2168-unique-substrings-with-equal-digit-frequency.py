class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n, s_set = len(s), set()
        for i in range(n):
            cur, cnt = "", [0] * 10
            for j in range(i, n):
                cnt[ord(s[j]) - ord("0")] += 1
                cur += s[j]
                if len(set(cnt) - {0}) == 1:
                    s_set.add(cur)
        return len(s_set)