class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        C, C2 = Counter(s), Counter(goal)
        dif = 0
        for c, d in zip(s, goal):
            if c != d:
                dif += 1
        if dif == 2:
            return C == C2
        if dif == 0:
            if any(v >= 2 for v in C.values()):
                return True
        return False