class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def enc(s):
            l, r = 0, 0
            res = []
            while l < len(s):
                res.append(s[l])
                while r < len(s) and s[l] == s[r]:
                    r += 1
                # s[l] != s[r] or r = len(s)
                res.append(r - l)
                l = r
            return res

        ss = enc(s)
        cnt = 0
        for ew in map(enc, words):
            if len(ss) != len(ew):
                continue
            for i, st in enumerate(zip(ss, ew)):
                x, y = st
                if i % 2 == 0 and x != y:
                    break
                if i % 2 == 1:
                    # math
                    if x == y or x > y and x >= 3:
                        continue
                    else:
                        break
            else:
                cnt += 1
                # print(ss, ew)
        return cnt