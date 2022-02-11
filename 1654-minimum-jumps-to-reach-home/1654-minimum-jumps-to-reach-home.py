class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque([(0, False, 0)])
        vis = set(forbidden)
        while q:
            pos, backed, jumps = q.popleft()
            if pos == x:
                return jumps

            pa, pb = pos + a, pos - b
            if pa < 6000 and pa not in vis:
                q.append((pa, False, jumps + 1))
                vis.add(pa)
            if not backed and pb > 0 and pb not in vis:
                q.append((pb, True, jumps + 1))
        return -1
