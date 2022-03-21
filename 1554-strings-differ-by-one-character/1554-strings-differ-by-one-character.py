class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        m = len(dict[0])
        rm_1_char = set()
        for w in dict:
            s = list(w)
            for i in range(m):
                s_rm1 = "".join(s[:i] + ["_"] + s[i + 1 :])
                if s_rm1 in rm_1_char:
                    return True
                rm_1_char.add(s_rm1)
        return False