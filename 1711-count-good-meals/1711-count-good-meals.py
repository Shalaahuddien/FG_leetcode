class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = Counter(deliciousness)
        res = 0
        for n in freq:
            for k in range(22):
                o = 2**k - n
                if o in freq:
                    if o != n:
                        res += freq[n] * freq[o]
                    else:
                        res += freq[n] * (freq[n] - 1)
                    # print(n, o, freq[n], freq[o], res)

        return (res // 2) % (10**9 + 7)