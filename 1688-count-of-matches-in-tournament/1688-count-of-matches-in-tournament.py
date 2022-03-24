class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        matches = 0
        while teams > 1:
            if teams % 2 == 1:
                teams = (teams - 1) // 2 + 1
                matches += teams - 1
            else:
                teams = teams // 2
                matches += teams
        return matches