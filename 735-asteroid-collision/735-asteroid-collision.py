class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] > -new:
                    break
                elif ans[-1] == -new:
                    ans.pop()
                    break
                else:
                    ans.pop()
                    continue
            else:
                ans.append(new)
        return ans
            