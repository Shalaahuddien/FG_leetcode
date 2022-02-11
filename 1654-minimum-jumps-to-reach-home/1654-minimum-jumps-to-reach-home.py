class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        vis = set(forbidden)
        key = -1
        UPPER = max(forbidden + [x]) + a + b

        def dfs(p, cnt, back):
            nonlocal key
            if key < 0 and 0 <= p <= UPPER:  # # 6000是往右探索的最大值，x最大为2000
                if p == x:  # 第一次遍历到 x时的次数即为结果，暂存结果，不再递归
                    key = cnt
                    return
                if p + a not in vis:
                    vis.add(p + a)  # 防止无限递归，比如 a = b 时，不加限制，就会出现无限递归
                    dfs(p + a, cnt + 1, 0)
                if p - b not in vis and back != 1:  # 若back为1说明上次就是往后跳的
                    dfs(p - b, cnt + 1, 1)

        dfs(0, 0, 0)
        return key