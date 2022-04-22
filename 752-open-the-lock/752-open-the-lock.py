class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q1, q2 = set(["0000"]), set([target])
        vis = set(["0000", target, *deadends])
        ops = 0
        while q1:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            q1_nxt = set()
            for code in q1:
                if code in q2:
                    return ops
                for i in range(4):
                    d = int(code[i])
                    for k in (d - 1) % 10, (d + 1) % 10:
                        cand = code[:i] + str(k) + code[i + 1 :]
                        if cand in q2:
                            return ops + 1
                        if cand not in vis:
                            vis.add(cand)
                            q1_nxt.add(cand)
            q1 = q1_nxt
            ops += 1
        return -1