class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        p_i = list([i, 0] for i in range(len(pieces)))
        last_sublist = -1
        for a in arr:
            if last_sublist == -1:
                for i, pi in enumerate(p_i):
                    pidx, it = pi[0], pi[1]
                    p = pieces[pidx]
                    if it < len(p) and p[it] == a:
                        last_sublist = i
                        it += 1
                        if it == len(p):
                            last_sublist = -1
                        else:
                            pi[1] = it
                        break
                else:
                    return False
            else:
                # in last_sublist
                pidx, it = p_i[last_sublist]
                p = pieces[pidx]
                if p[it] != a:
                    return False
                it += 1
                if it == len(p):
                    last_sublist = -1
                else:
                    p_i[last_sublist][1] = it
        return True