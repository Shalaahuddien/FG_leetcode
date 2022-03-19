class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        last_is_two = False
        while i < len(bits):
            if bits[i] ==0:
                i += 1
                last_is_two = False
            else:
                i += 2
                last_is_two = True
        return last_is_two == False
