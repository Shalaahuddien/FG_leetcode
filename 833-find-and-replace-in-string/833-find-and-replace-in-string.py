class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        tmp = []
        pre = 0
        mp = {idx: i for i, idx in enumerate(indices)}
        sortedindices = sorted(indices)
        for i in sortedindices:
            if not i >= pre:
                continue
            ori = mp[i]
            src = sources[ori]
            l = len(src)
            tar = targets[ori]
            tmp.append(s[pre:i])
            if s[i : i + l] == src:
                tmp.append(tar)
            else:
                tmp.append(s[i : i + l])
            pre = i + l
        tmp.append(s[pre:])
        return "".join(tmp)