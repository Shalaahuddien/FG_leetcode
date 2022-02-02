class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def req(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)

        c = Counter(ages)
        return sum(c[a] * (c[b] - (a == b)) for a in c for b in c
                   if req(a, b))
