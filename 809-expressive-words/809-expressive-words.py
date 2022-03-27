class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def enc(s):
            res = []
            for k, grp in groupby(s):
                res.append([k, len(list(grp))])
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