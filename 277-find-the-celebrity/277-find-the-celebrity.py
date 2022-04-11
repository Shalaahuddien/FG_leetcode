# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True

        candidate = 0
        # step 1: narrow down candidate
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        # step 2: verify it's REAL celebrity
        if is_celebrity(candidate):
            return candidate
        return -1
