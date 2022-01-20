class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        xor = piles[0]
        for i in range(1, len(piles)):
            xor ^= piles[i]
        if xor == 0:
            return False
        return True