class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        locked_open, unlocked = [], []
        for i, c in enumerate(s):
            if locked[i] == "0":
                unlocked.append(i)
            else:
                if c == "(":
                    locked_open.append(i)
                else:
                    if locked_open:
                        locked_open.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False
        while locked_open:
            if unlocked and unlocked[-1] > locked_open[-1]:
                unlocked.pop()
                locked_open.pop()
            else:
                return False
        return True