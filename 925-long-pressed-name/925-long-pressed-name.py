class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j,m,n = 0,0,len(name),len(typed)
        while j < n:
            if i < m and name[i] == typed[j]:
                i += 1
            elif not (j > 0 and typed[j-1] == typed[j]):
                return False
            j += 1
        return i == m