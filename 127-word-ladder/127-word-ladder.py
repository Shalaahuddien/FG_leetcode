class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l = 2
        front, back = set([beginWord]), set([endWord])
        wordDict = set(wordList)
        wordDict.discard(beginWord)
        if endWord not in wordDict:
            return 0
        while front:
            # generate all valid transform (aka goto neighbor)
            front = wordDict & (set(word[:i] + ch + word[i + 1:]
                                    for word in front
                                    for i in range(len(beginWord))
                                    for ch in ascii_lowercase))
            if front & back:
                return l
            l += 1
            if len(front) > len(back):
                front, back = back, front
            # remove transforms from wordDict to avoid cycle
            wordDict -= front
        return 0