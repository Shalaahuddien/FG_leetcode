class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        minheap = []
        for r in range(min(k,m)):
            heappush(minheap, (matrix[r][0], r,0))
        ans = -1
        for i in range(k):
            ans, r,c = heappop(minheap)
            if c+1 < m:
                heappush(minheap, (matrix[r][c+1],r,c+1))
        return ans