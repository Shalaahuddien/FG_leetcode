class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # a,b,c,d = d,a,b,c
        # i,j => j,n-i-1 => n-i-1, n-j-1 => n-j-1,i
        # range: r in (N//2), c in (N+1//2)
        n = len(M)
        for i in range(n//2):
            for j in range((n+1)//2):
                M[i][j], M[j][n-i-1], M[n-i-1][n-j-1], M[n-j-1][i] = \
                    M[n-j-1][i],  M[i][j], M[j][n-i-1], M[n-i-1][n-j-1]
        