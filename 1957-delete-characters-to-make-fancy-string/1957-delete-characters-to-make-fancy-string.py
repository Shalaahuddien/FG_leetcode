class Solution:
    def makeFancyString(self, s: str) -> str:
        l = r = 0
        cnt = 0
        ls = list(s)

        while l < len(ls):
            while r < len(ls) and ls[r] == ls[l]:
                if cnt >= 2:
                    ls[r] = ""
                r += 1
                cnt += 1
            # r oor or ls[r] != ls[l], found segment [l:r]
            cnt = 0
            l = r

        return "".join(ls)