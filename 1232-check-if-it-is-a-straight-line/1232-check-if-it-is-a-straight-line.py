class Solution:
    def checkStraightLine(self, CO: List[List[int]]) -> bool:
        def slope(P,Q):
            if P[0] == Q[0]:
                return math.inf
            return (Q[1] - P[1]) / (Q[0] - P[0])

        sl = None
        for i in range(1, len(CO)):
            if i == 1:
                sl = slope(CO[i], CO[i - 1])
            else:
                if sl != slope(CO[i], CO[i - 1]):
                    return False
        return True