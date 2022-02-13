# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def count(sea: 'Sea', P: Point, Q: Point):
            res = 0
            if P.x >= Q.x and P.y >= Q.y and sea.hasShips(P, Q):
                if P.x == Q.x and P.y == Q.y:
                    return 1
                mx, my = (P.x + Q.x) // 2, (P.y + Q.y) // 2
                res += count(sea, P, Point(mx + 1, my + 1))
                res += count(sea, Point(mx, P.y), Point(Q.x, my + 1))
                res += count(sea, Point(mx, my), Q)
                res += count(sea, Point(P.x, my), Point(mx + 1, Q.y))
            return res
        return count(sea, topRight, bottomLeft)
