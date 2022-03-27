class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def enc(s):
            l, r = 0, 0
            res = []
            while l < len(s):
                # res.append(s[l])
                while r < len(s) and s[l] == s[r]:
                    r += 1
                # s[l] != s[r] or r = len(s)
                res.append((s[l], r - l))
                l = r
            return res

        ss = enc(s)
        cnt = 0
        for ew in map(enc, words):
            if len(ss) != len(ew):
                continue
            for i in range(len(ss)):
                if ss[i][0] != ew[i][0]:
                    break
                if not (ss[i][1] == ew[i][1] or ss[i][1] >= max(3, ew[i][1])):
                    break
            else:
                cnt += 1
                # print(ss, ew)
        return cnt