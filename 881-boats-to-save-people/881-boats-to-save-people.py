class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        q = deque(people)
        boats = 0
        while q:
            if len(q) == 1:
                return boats+1
            if q[0] + q[-1] > limit:
                q.pop()
            else:
                q.popleft()
                q.pop()
            boats += 1
        return boats
