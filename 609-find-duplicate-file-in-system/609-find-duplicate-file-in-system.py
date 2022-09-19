class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        v2p = defaultdict(list)
        res = []
        for l in paths:
            tmp = l.split()
            p, fs = tmp[0], tmp[1:]
            for f in fs:
                ftmp = f.split("(")
                fn, fv = ftmp[0], str(ftmp[1][:-1])
                # print(f"{fn=}, {fv=}")
                v2p[fv].append(f"{p}/{fn}")
        for p in v2p.values():
            if len(p) > 1:
                res.append(p)
        return res