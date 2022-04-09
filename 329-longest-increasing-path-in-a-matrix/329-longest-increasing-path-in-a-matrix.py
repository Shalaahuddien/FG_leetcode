class Solution:
    def longestIncreasingPath(self, M: List[List[int]]) -> int:
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # step 1: build a DAG
        AL = defaultdict(list)
        IND = defaultdict(int)
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                neighbors = [(i + dx, j + dy) for dx, dy in DIR]
                for x, y in neighbors:
                    if 0 <= x < m and 0 <= y < n and M[i][j] < M[x][y]:
                        AL[(i, j)].append((x, y))
                        IND[(x, y)] += 1
        # step 2: Topo-sort w/ Kahn's algs
        q = deque([(i, j) for i in range(m) for j in range(n) if (i, j) not in IND])
        mx_path_len = 0
        while q:
            mx_path_len += 1
            for _ in range(len(q)):
                node = q.popleft()
                for neigh in AL[node]:
                    IND[neigh] -= 1
                    if not IND[neigh]:
                        q.append(neigh)
        return mx_path_len