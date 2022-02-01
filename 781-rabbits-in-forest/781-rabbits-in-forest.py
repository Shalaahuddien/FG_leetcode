class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d,res = {}, 0
        for i in answers:
            if i == 0:
                res += 1
            else:
                if i not in d or i == d[i]:
                    d[i] = 0
                    res += 1 + i
                else:
                    d[i] += 1
        return res
    