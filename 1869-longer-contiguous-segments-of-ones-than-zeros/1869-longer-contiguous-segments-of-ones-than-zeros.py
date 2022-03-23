class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mx0, mx1 = 0, 0
        cnt = 0
        prev = "#"
        for c in s + "#":
            if prev == c:
                cnt += 1
            else:
                if prev == "0":
                    mx0 = max(mx0, cnt)
                elif prev == "1":
                    mx1 = max(mx1, cnt)
                cnt = 1
            prev = c
        return mx1 > mx0