class Solution:
    def maximumTime(self, time: str) -> str:
        ss = list(time)
        for i, t in enumerate(time):
            if t != "?":
                continue
            if i == 0:
                ss[i] = "2" if ss[i + 1] in "?0123" else "1"
            elif i == 1:
                ss[i] = "3" if ss[0] == "2" else "9"
            elif i == 3:
                ss[i] = "5"
            else:
                ss[i] = "9"
        return "".join(ss)