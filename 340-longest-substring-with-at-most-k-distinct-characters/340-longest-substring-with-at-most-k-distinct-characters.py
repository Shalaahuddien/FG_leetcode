class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res, l, r = 0, 0, 0
        cnt = Counter()
        dst = 0
        while r < len(s):
            c = s[r]
            if cnt[c] == 0: dst += 1
            cnt[c] += 1
            r += 1
            while dst > k:
                d = s[l]
                cnt[d] -= 1
                if cnt[d] == 0: dst -= 1
                l += 1
            # now dst <= k
            res = max(res, r - l)
        return res