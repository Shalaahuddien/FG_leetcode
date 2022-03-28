class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        intervals = []
        words.sort(key=lambda x: -len(x))
        for i in range(len(s)):
            for w in words:
                if s[i:].startswith(w):
                    intervals.append([i, i + len(w)])

        def merge(I):
            res = []
            for itv in I:
                if not res or res[-1][1] < itv[0]:
                    res.append(itv)
                else:
                    res[-1][1] = max(res[-1][1], itv[1])
            return res

        merged = merge(intervals)
        res, prev_end = [], 0
        for start, end in merged:
            res.append(s[prev_end:start] + "<b>" + s[start:end] + "</b>")
            prev_end = end
        return "".join(res + [s[prev_end:]])