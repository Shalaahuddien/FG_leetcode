class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, m, n = 0, 0, len(name), len(typed)
        while j < n:
            # case 1: matched, incr both i&j
            if i < m and name[i] == typed[j]:
                i += 1
            # case 2: unmatch, must be streched (aka typed is [ee])
            elif j > 0 and typed[j - 1] == typed[j]:
                pass
            else:
                return False
            j += 1
        return i == m