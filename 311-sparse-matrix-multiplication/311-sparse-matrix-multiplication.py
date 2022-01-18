class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def constructmap(mat):
            hashmap = {}
            rows, cols = len(mat), len(mat[0])
            for r in range(rows):
                for c in range(cols):
                    if mat[r][c] != 0:
                        hashmap[(r, c)] = mat[r][c]
            return hashmap

        map1, map2 = constructmap(mat1), constructmap(mat2)

        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        res = [[0 for _ in range(n)] for _ in range(m)]

        for pos1, val1 in map1.items():
            for pos2, val2 in map2.items():
                if pos1[1] == pos2[0]:
                    res[pos1[0]][pos2[1]] += val1 * val2

        return res