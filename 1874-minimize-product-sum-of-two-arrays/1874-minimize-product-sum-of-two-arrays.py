class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        counter1, counter2 = [0] * 101, [0] * 101
        m, n = len(nums1), len(counter1)

        # fill buckets
        for i in range(m):
            counter1[nums1[i]] += 1
            counter2[nums2[i]] += 1

        # meet in the middle and multiply at each end
        p1, p2, prod_sum = 0, n - 1, 0
        while 0 < p2 and p1 < n:
            while p1 < n and not counter1[p1]:
                p1 += 1
            while 0 < p2 and not counter2[p2]:
                p2 -= 1
            if 0 < p2 and p1 < n and counter1[p1] and counter2[p2]:
                occ = min(counter1[p1], counter2[p2])
                prod_sum += occ * p1 * p2
                counter1[p1] -= occ
                counter2[p2] -= occ
        return prod_sum