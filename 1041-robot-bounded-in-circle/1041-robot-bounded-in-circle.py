class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north
        d = 0
        for ins in instructions:
            if ins == 'G':
                dx, dy = DIR[d]
                x, y = x + dx, y + dy
            elif ins == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
        if x == y == 0 or d != 0:
            return True
        return False