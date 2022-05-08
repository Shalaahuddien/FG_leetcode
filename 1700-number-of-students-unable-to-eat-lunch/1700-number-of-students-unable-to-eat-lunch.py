class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        n,k = len(students), 0
        while k < n and cnt[sandwiches[k]]:
            cnt[sandwiches[k]] -= 1
            k += 1
        return n-k