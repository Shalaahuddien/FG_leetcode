class Solution:
    def alienOrder(self, words: List[str]) -> str:
        AL = {c: set() for w in words for c in w}

        # step 1: build AL of char
        for fir, sec in zip(words, words[1:]):
            # XXX: for case ["abc","ab"]
            lenmin = min(len(fir), len(sec))
            if len(fir) > len(sec) and fir[:lenmin] == sec[:lenmin]:
                return ''
            for c, d in zip(fir, sec):
                if c != d:
                    AL[c].add(d)
                    break

        # step 2: CLRS 3-color DFS & post-order traversal for toposort/cycle detection
        WHITE, GRAY, BLACK = 0, 1, 2
        colr = defaultdict(int)
        ts = []

        def dfs_color(c):
            if colr[c] != WHITE:
                return colr[c] == BLACK  # if gray, then cycle detected
            colr[c] = GRAY
            for v in AL[c]:
                if colr[v] == GRAY or not dfs_color(v):
                    return False  # cycle detected lower down
            colr[c] = BLACK
            ts.append(c)
            return True  # write framework first, before recursion, as Neet does!

        # for DFS toposort, we need to call dfs on ALL nodes, just like CC!
        if not all(dfs_color(c) for c in AL):
            return ''
        return ''.join(ts[::-1])