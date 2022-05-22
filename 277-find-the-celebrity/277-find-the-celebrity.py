# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def is_celebrity(cand):
            for o in range(n):
                if cand == o:
                    continue
                if knows(cand, o) or not knows(o, cand):
                    return False
            return True
        
        cand = 0
        for i in range(n):
            if knows(cand, i):
                cand = i
        if is_celebrity(cand):
            return cand
        return -1