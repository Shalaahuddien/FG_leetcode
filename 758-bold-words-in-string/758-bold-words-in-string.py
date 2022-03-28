class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        intervals = []
        words.sort(key=lambda x: -len(x))
        for i in range(len(s)):
            for w in words:
                if s[i:].startswith(w):
                    intervals.append([i, i + len(w) - 1])

        def merge(I):
            if not I:
                return []

            res = []
            l, r = I[0]
            for i, j in intervals[1:]:
                if i > r+1:
                    res.append((l, r))
                    l, r = i, j
                else:
                    r = max(r, j)
            res.append((l, r))
            return res

        merged = merge(intervals)
        # print(intervals)
        # print(merged)

        ss = list(s)
        for l, r in merged:
            ss[l] = "<b>" + ss[l]
            ss[r] = ss[r] + "</b>"
        return "".join(ss)