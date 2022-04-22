class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q1, q2 = set([start]), set([goal])
        step = 0
        vis = set([start, goal])
        while q1:
            # 交换队列大小，保证BFS总是展开小的那一侧
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            q1_nxt = set()
            for v in q1:
                # if v in q2:
                #     return step
                for n in nums:
                    for vv in (v + n, v - n, v ^ n):
                        if vv in q2:
                            return step + 1
                        if vv in vis or not 0 <= vv <= 1000:
                            continue
                        vis.add(vv)
                        q1_nxt.add(vv)
            q1 = q1_nxt
            step += 1
        return -1