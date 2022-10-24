class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [word for word in arr if len(set(word)) == len(word)]
        
        d = {}
        for i, word in enumerate(arr):
            d[1<<i] = (sum(1<<(ord(w) - 97) for w in word), len(word))

        @cache
        def dp(m):
            if m == 0: return (0, 0)
            prev = m & (m - 1)
            m_last, bits_last = dp(prev)
            if m_last & d[m - prev][0] != 0: return (0, -10000)
            return (m_last | d[m - prev][0], bits_last + d[m - prev][1])
        
        return max(dp(x)[1] for x in range(1<<len(arr)))