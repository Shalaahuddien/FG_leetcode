class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def none_zeros(M):
            mp = {}
            for r in range(len(M)):
                for c in range(len(M[0])):
                    if M[r][c] != 0:
                        mp[(r,c)] = M[r][c]
            return mp
        sparse_1, sparse_2 = none_zeros(mat1), none_zeros(mat2)
        n,m,k = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0]*k for _ in range(n)]
        for pos1, v1 in sparse_1.items():
            for pos2, v2 in sparse_2.items():
                if pos1[1] == pos2[0]:
                    res[pos1[0]][pos2[1]] += v1*v2
        return res
                