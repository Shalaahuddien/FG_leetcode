class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache
        def dp(r,c):
            if c < 0 or c > r: return 0
            if r == c == 0: return poured
            return max(0, dp(r-1,c-1)-1)/2 + max(0, dp(r-1,c)-1)/2
        
        return min(1, dp(query_row, query_glass))