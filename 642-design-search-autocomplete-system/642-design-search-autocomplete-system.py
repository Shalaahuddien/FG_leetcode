class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.top3 = []


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, sentence, time):
        p = self.root
        for c in sentence:
            p = p.child[c]
            for i, (t, s) in enumerate(p.top3):
                if s == sentence:
                    tmp = p.top3
                    tmp[i][0] = time
                    break
            else:  # for-else means no break => sentence not in node.top3
                tmp = p.top3 + [[time, sentence]]
            # sort by time desc, then break tie by lexico order of sentence asc
            p.top3 = sorted(tmp, key=lambda x: (-x[0], x[1]))[:3]


class AutocompleteSystem:
    """

    https://leetcode.com/problems/design-search-autocomplete-system/discuss/1562242/Python-3-or-Trie-Variation-or-Explanation
    """
    def __init__(self, sentences: List[str], times: List[int]):
        self.d = Counter()  # keep tracking {sentence: time}
        self.trie = Trie()  # trie
        self.node = self.trie.root  # pointer to root and move along with input characters
        for s, t in zip(sentences, times):  # init trie
            self.d[s] += t
            self.trie.add(s, t)
        self.buf = ''  # prefix
        self.prefix_non = False  # True if prefix cannot be found

    def input(self, c: str) -> List[str]:
        if c == '#':  # input ends
            self.node = self.trie.root
            self.d[self.buf] += 1
            self.trie.add(self.buf, self.d[self.buf])
            self.buf = ''
            self.prefix_non = False  # reset flag
            return []

        # when inputing the sentence
        self.buf += c  # making prefix
        # when prefix is not found the first time and time after 1st time
        if c not in self.node.child or self.prefix_non:
            self.prefix_non = True  # set flag
            return []
        self.prefix_non = False  # reset flag
        self.node = self.node.child[c]
        return [stn for _, stn in self.node.top3]
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)