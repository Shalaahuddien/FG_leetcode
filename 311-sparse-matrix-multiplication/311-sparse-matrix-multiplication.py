class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        I, J = len(mat1), len(mat1[0])
        K = len(mat2[0])

        nzj1, nzj2 = set(), set()

        nz1 = defaultdict(set)
        for i in range(I):
            for j in range(J):
                if mat1[i][j]:
                    nz1[j].add((i))
                    nzj1.add(j)

        nz2 = defaultdict(set)
        for j in range(J):
            for k in range(K):
                if mat2[j][k]:
                    nz2[j].add((k))
                    nzj2.add(j)

        ans = [[0] * K for _ in range(I)]

        for j in nzj1.intersection(nzj2):
            for i in nz1[j]:
                for k in nz2[j]:
                    ans[i][k] += mat1[i][j] * mat2[j][k]
        return ans
