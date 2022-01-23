class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = '123456789'
        n = 10
        nums = []
        for le in range(len(str(low)), len(str(high))+1):
            for start in range(n-le):
                v = int(sample[start:start+le])
                if low <= v <= high:
                    nums.append(v)
                    
        return nums