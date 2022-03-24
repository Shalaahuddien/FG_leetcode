class Solution:
    def minTimeToType(self, word: str) -> int:
        def o(c,d):
            return (ord(c) - ord(d)) % 26
        pre = 'a'
        ans = len(word)
        for c in word:
            val = o(c,pre)
            ans += min(val, 26-val)
            pre = c
        return ans

        