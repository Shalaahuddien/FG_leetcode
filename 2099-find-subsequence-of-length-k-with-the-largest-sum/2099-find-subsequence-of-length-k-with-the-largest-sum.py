class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partition(b, e):
            r = randint(b, e)
            swap(r, e)
            p = nums[e]

            l = b - 1
            for i in range(b, e):
                if -nums[i] < -p:
                    l += 1
                    swap(l, i)
            swap(l + 1, e)
            return l + 1

        def qselect():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = partition(l, r)
                if mid == k:
                    break
                elif mid < k:
                    l = mid + 1
                else:
                    r = mid

        numscopy = nums[:]
        qselect()
        ans = []
        C = Counter(nums[:k])
        for n in numscopy:
            if C[n] > 0:
                C[n] -= 1
                ans.append(n)
        return ans