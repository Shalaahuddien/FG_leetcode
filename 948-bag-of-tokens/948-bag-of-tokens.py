class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j, score, opt = 0, len(tokens) - 1, 0, 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                i += 1
                score += 1
                opt = max(opt, score)
            elif score >= 1:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break
        return opt