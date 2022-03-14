class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = {t: [0] * 26 + [t] for t in votes[0]}
        for vote in votes:
            for r, v in enumerate(vote):
                ranks[v][r] -= 1
        ranks_list = list(ranks.values())
        ranks_list.sort()
        res = []
        for r in ranks_list:
            res.append(r[-1])
        return "".join(res)