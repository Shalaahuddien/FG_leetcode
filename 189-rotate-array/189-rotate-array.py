class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        start_idx = count = 0
        while count < n:
            cur_idx, tmp = start_idx, nums[start_idx]
            while True:
                nxt_idx = (cur_idx + k) % n
                nums[nxt_idx], tmp = tmp, nums[nxt_idx]
                cur_idx = nxt_idx
                count += 1

                if start_idx == cur_idx:
                    break
            start_idx += 1