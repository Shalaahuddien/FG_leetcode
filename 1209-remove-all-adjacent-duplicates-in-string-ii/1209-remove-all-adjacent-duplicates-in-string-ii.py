class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []  # hold pair of [char, freq]
        for c in s:
            if not stk or stk[-1][0] != c:
                stk.append([c, 1])
            else:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
        return "".join(c * cnt for c, cnt in stk)