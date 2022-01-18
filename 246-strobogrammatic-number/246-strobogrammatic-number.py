class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8}
        i, j = 0, len(num)-1
        while i <= j:
            x, y = int(num[i]), int(num[j])
            if x not in mp or y not in mp:
                return False
            if x != mp[y]:
                return False
            i, j = i+1, j-1
        return True