class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans, st = 0, []
        for _, df in properties:
            while st and st[-1] < df:
                st.pop()
                ans += 1
            st.append(df)
        return ans