class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans, cnt = [], Counter(s)
        for c in order:
            if cnt[c]:
                ans.extend([c] * cnt.pop(c))
        for c, f in cnt.items():
            ans.extend(c * f)
        return "".join(ans)