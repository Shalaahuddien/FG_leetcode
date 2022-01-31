class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal: return len(set(s)) < len(s)
        dif = [(a,b) for a,b in zip(s,goal) if a!=b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]