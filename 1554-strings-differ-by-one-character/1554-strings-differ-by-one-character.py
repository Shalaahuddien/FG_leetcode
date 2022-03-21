class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        m = len(dict[0])
        rm_1_char = defaultdict(int)
        for w in dict:
            s = list(w)
            for i in range(m):
                s_rm1 = "".join(s[:i] + ["_"] + s[i + 1 :])
                rm_1_char[s_rm1] += 1
                # if rm_1_char[s_rm1] > 2:
                #     return False
        # print(rm_1_char)
        return any(f >= 2 for f in rm_1_char.values())