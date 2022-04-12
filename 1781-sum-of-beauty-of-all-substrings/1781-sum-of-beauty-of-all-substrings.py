class Solution:
    def beautySum(self, s: str) -> int:
        beauty, n = 0, len(s)
        for l in range(3, n + 1):
            cnt = Counter()
            for j in range(l):
                cnt[s[j]] += 1
            beauty += max(cnt.values()) - min(cnt.values())
            for j in range(l, n):
                cnt[s[j]] += 1
                cnt[s[j - l]] -= 1
                if cnt[s[j - l]] == 0:
                    del cnt[s[j - l]]
                beauty += max(cnt.values()) - min(cnt.values())
        return beauty
