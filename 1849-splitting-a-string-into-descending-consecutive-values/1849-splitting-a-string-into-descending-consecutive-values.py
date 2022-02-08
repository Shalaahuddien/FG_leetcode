class Solution:
    def splitString(self, s: str) -> bool:
        def bt(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s) + 1):
                cut = s[:i]
                if not cut:
                    continue
                if not path or int(cut) + 1 == path[-1]:
                    bt(s[i:], path + [int(cut)], res)

        res = []
        bt(s, [], res)
        return len(res) > 1