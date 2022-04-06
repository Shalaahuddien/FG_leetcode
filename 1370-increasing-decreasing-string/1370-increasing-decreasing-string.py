class Solution:
    def sortString(self, s: str) -> str:
        cnt, ans, asc = Counter(s), [], True
        while cnt:
            for c in sorted(cnt) if asc else reversed(sorted(cnt)):
                ans.append(c)
                cnt[c] -= 1
                if cnt[c] == 0:
                    cnt.pop(c)
            asc = not asc
        return "".join(ans)
