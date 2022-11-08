class Solution:
    def makeGood(self, s: str) -> str:
        st = [s[0]]
        for c in s[1:]:
            if st and st[-1] != c and st[-1].upper() == c.upper():
                st.pop()
            else:
                st.append(c)
        return ''.join(st)
        