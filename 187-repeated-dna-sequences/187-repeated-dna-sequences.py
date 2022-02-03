class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []

        # rolling hash: transform to base-4!
        a = 4
        aL = pow(a, L)

        # convert str to list[int]
        atoi = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [atoi[c] for c in s]

        h = 0
        seen, output = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            # compute hash
            else:
                for i in range(L):
                    h = h * a + nums[i]
            # update output and hashset of seen seq
            if h in seen:
                output.add(s[start:start + L])
            seen.add(h)
        return output
