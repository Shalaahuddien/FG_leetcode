class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def slide(numUniqueTarget):
            l = r = numUnique = numAtLeastK = count = 0
            freq = Counter()
            while r < len(s):
                c = s[r]
                if freq[c] == 0:
                    numUnique += 1
                freq[c] += 1
                if freq[c] == k:
                    numAtLeastK += 1
                r += 1

                while numUnique > numUniqueTarget:
                    d = s[l]
                    if freq[d] == k:
                        numAtLeastK -= 1
                    freq[d] -= 1
                    if freq[d] == 0:
                        numUnique -= 1
                    l += 1
                if numUnique == numAtLeastK:
                    count = max(count, r - l)
            return count

        mxcount = 0
        for i in range(1, 27):
            mxcount = max(mxcount, slide(i))
        return mxcount