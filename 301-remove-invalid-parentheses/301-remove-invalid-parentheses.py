class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isval(p):
            bal = 0
            for c in p:
                if c == '(':
                    bal += 1
                elif c == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        ans = []  # !indicate whether a valid node has been met as well
        seen = set([s])
        q = deque([(s, 0)])
        while q:
            for _ in range(len(q)):
                cur, rm = q.popleft()
                if isval(cur):
                    ans.append(cur)

                if not ans:  # ! if not valid node has been met
                    for i in range(len(cur)):
                        nei = ''.join(cur[:i] + cur[i + 1:])
                        if nei not in seen:
                            q.append((nei, rm + 1))
                            seen.add(nei)
            if ans:  # ! if valid node met, other valid nodes also in same level, so we can terminate after this level
                break
        return ans