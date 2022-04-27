class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            vis.add(i)
            group.append(i)
            for j in AL[i]:
                if j not in vis:
                    dfs(j)

        vis = set()
        n = len(s)
        AL = defaultdict(list)
        for i, j in pairs:
            AL[i].append(j)
            AL[j].append(i)
        lst = list(s)
        for i in range(n):
            if i not in vis:
                group = []
                dfs(i)
                group.sort()
                chars = [lst[k] for k in group]
                chars.sort()
                for i in range(len(group)):
                    lst[group[i]] = chars[i]
        return "".join(lst)