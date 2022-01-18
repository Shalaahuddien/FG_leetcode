class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d1 = '01869'
        d2 = '01896'
        mp = {}
        for a,b in zip(d1,d2):
            mp[a] = b
        
        l,r = 0, len(num)-1
        while l <= r:
            a,b = num[l],num[r]
            if a not in mp or b not in mp:
                return False
            if mp[a] != b:
                return False
            l,r = l+1,r-1
        return True