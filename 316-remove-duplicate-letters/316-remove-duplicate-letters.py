class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        in_stk = set()
        last_pos = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            # this is to maintain only one of each character
            if c in in_stk:
                continue

            # piecewise mono-incr stack
            while stk and c < stk[-1] and i < last_pos[stk[-1]]:
                in_stk.remove(stk.pop())
            stk.append(c)
            in_stk.add(c)

        return "".join(stk)