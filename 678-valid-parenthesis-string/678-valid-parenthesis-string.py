class Solution:
    def checkValidString(self, s: str) -> bool:
        def validate(s, op):
            bal, wild = 0, 0
            for p in s:
                if p in "()":
                    bal += 1 if p == op else -1
                else:
                    wild += 1
                if wild + bal < 0:
                    return False
            return bal <= wild

        return validate(s, "(") and validate(s[::-1], ")")
