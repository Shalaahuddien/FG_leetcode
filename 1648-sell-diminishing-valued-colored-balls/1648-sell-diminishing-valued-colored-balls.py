class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        A = inventory
        A.sort()
        A = [0] + A
        r = len(A) - 1
        gain = 0

        def sm(v, num):
            last, fir = v, v - num + 1
            return (fir + last) * num // 2

        while orders:
            less_idx = bisect_left(A, A[r]) - 1
            less = A[less_idx]
            batch = r - less_idx
            diff = A[r] - less
            bought = min(orders, diff * batch)
            num_batch, last_batch = divmod(bought, batch)
            if num_batch:
                for i in range(less_idx + 1, r + 1):
                    gain += sm(A[i], num_batch)
                    A[i] -= num_batch
            for i in range(less_idx + 1, less_idx + 1 + last_batch):
                gain += A[i]
                A[i] -= 1
            orders -= bought
            # for i in range(less_idx + 1, r + 1):
            #     if orders != 0 and A[i] > less:
            #         gain += A[i]
            #         A[i] -= 1
            #         orders -= 1
        return gain % MOD