class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Classic Greedy. Thinking process is more import than code.
        
        """
        class LargestNumKey(str):
            def __lt__(x,y):
                return x+y > y+x
        largest_num = ''.join(sorted(map(str, nums), key=LargestNumKey))
        return '0' if largest_num[0] == '0' else largest_num
