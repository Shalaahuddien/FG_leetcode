class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        root, n, intervals = {}, len(s), []
        # create trie
        for w in words:
            cur = root
            for c in w:
                cur = cur.setdefault(c, {})
            cur["#"] = 0

        # interval merge
        def merge_interval(iv):
            if not intervals or intervals[-1][1] < iv[0]:
                intervals.append(iv)
            else:
                intervals[-1][1] = max(intervals[-1][1], iv[1])

        # make max match and add to interval
        for i in range(n):
            cur, mx_end = root, None
            for j in range(i, n):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if "#" in cur:
                    mx_end = j + 1  # jem: [i,j+1)
            # !only need to add max-match interval!
            if mx_end:
                merge_interval([i, mx_end])
        # concat result
        res, prev_end = [], 0
        for l, r in intervals:
            res.append(s[prev_end:l] + "<b>" + s[l:r] + "</b>")
            prev_end = r
        return "".join(res + [s[prev_end:]])