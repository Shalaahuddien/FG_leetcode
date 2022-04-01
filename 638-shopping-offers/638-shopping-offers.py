class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @cache
        def dp(needs):
            # not take offer
            cost = sum(n * price[i] for i, n in enumerate(needs))
            # take one offer
            for offer in special:
                for i, n in enumerate(needs):
                    if n < offer[i]:
                        break
                else:
                    new_needs = tuple([n - offer[i] for i, n in enumerate(needs)])
                    # update cost
                    cost = min(cost, offer[-1] + dp(new_needs))
            return cost

        return dp(tuple(needs))