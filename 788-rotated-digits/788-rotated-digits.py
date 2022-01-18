class Solution:
    def rotatedDigits(self, n: int) -> int:
        remains, skips, count = '2569', '347', 0

        for val in range(1, n + 1):
            val = str(val)
            if any(skip in val for skip in skips): continue
            if any(remain in val for remain in remains): count += 1
        return count