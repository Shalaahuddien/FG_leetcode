class Vector2D:

    def __init__(self, vec2d):
        self.vec2d, self.x, self.y = vec2d, 0, 0
        while self.y < len(self.vec2d) and not self.x < len(self.vec2d[self.y]):
            self.x, self.y = 0, self.y + 1
                
        
    def next(self):
        ans = self.vec2d[self.y][self.x]
        self.x += 1
        while self.y < len(self.vec2d) and not self.x < len(self.vec2d[self.y]):
            self.x, self.y = 0, self.y + 1
        return ans
        
    def hasNext(self):
        return self.y < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()