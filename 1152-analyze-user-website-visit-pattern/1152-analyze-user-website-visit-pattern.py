class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[u].append(w)

        patterns = Counter()
        for u, webs in users.items():
            patterns.update(Counter(set(combinations(webs, 3))))
        return max(sorted(patterns), key=patterns.get)