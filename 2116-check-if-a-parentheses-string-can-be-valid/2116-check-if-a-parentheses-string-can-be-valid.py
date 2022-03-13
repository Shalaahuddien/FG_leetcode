class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def validate(s, locked, op):
            bal, wild = 0,0
            for i,p in enumerate(s):
                if locked[i] == "1":
                    bal += 1 if p == op else -1
                else:
                    wild += 1
                if wild + bal < 0:
                    return False
            return bal <= wild
        
        return len(s) % 2 == 0 and validate(s,locked, '(') and validate(s[::-1], locked[::-1], ')')