class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        mp = "0123456789abcdef"
        res = []
        # if neg (2's complement)
        if num < 0:
            num += 2**32
        while num:
            num, d = divmod(num, 16)
            res.append(mp[d])
        return "".join(res[::-1])