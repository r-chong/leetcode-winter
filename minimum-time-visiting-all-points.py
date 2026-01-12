class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # for each point, check the categorization of the delta: vert, horiz, or diag
        prev = points[0]
        t = 0

        for i in range(1, len(points)):
            cur = points[i]
            
            cd = self.chebyshev(prev[0], cur[0], prev[1], cur[1])

            t += cd

            prev = cur

        return t
    
    def chebyshev(self, x1, x2, y1, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        return min(dx, dy) + (max(dx, dy) - min(dx,dy))

# divergences:
# didn't use abs for delta
# used dx and dy direct instead of thinking of an algorithm (chebyshev or manhattan)