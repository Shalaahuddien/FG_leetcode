class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        binary = bin(num)[2:]
        for bit in binary:
            if bit == "1":
                steps += 2
            else:
                steps += 1
        return steps - 1