class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(piles):
            # state has no relation to order: [1,2,3]  = [2, 3,1] = ...
            if sum(piles) == 0:
                # Lose if no pile to remove
                return False

            lpiles = list(piles)
            for i in range(len(lpiles)):
                for x in range(1, lpiles[i] + 1):
                    lpiles[i] -= x
                    # For each pile try to remove any number, if any can cause the opponent lose, then win.
                    if not dfs(tuple(sorted(lpiles))):
                        return True
                    ## backtracking
                    lpiles[i] += x
            return False

        # make [1,2,3] to '123'
        return dfs(tuple(sorted(piles)))
