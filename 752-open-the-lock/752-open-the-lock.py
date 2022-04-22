class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        q = deque([(0, "0000")])
        if "0000" in dead:
            return -1
        while q:
            steps, code = q.popleft()
            if code == target:
                return steps

            for i in range(4):
                d = int(code[i])
                for k in (d - 1) % 10, (d + 1) % 10:
                    cand = code[:i] + str(k) + code[i + 1 :]
                    if cand not in dead:
                        dead.add(cand)
                        q.append((steps + 1, cand))
        return -1