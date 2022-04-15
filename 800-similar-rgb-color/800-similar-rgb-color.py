class Solution:
    def similarRGB(self, color: str) -> str:
        def f(c):
            ans = 0
            for k in range(1, 16):
                ans = min(ans, k * 16 + k, key=lambda x: abs(x - int(c, 16)))
            return hex(ans)[2:].zfill(2)

        return "#" + "".join(f(color[i : i + 2]) for i in (1, 3, 5))
