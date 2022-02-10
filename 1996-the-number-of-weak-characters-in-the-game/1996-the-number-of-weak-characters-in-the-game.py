class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans, mxdf = 0,0
        for _, df in properties:
            if df < mxdf:
                ans += 1
            else:
                mxdf = df
        return ans
    