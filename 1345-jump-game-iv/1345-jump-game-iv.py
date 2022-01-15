class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        G = defaultdict(list)
        for i, v in enumerate(arr):
            G[v].append(i)

        step = 0
        q = deque([0])
        vis = set()
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == n - 1:
                    return step

                v = arr[cur]
                # add all same v's index
                for i in G[v]:
                    if i not in vis:
                        vis.add(i)
                        q.append(i)

                del G[v]
                for i in {cur - 1, cur + 1}:
                    if 0 <= i < n and i not in vis:
                        vis.add(i)
                        q.append(i)
            step += 1

        return -1