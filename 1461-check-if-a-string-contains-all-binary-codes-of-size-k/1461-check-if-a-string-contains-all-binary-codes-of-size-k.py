class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        for i in range(k, len(s) + 1):
            st.add(s[i - k : i])
            if len(st) == 1 << k:
                break
        return len(st) == 1 << k