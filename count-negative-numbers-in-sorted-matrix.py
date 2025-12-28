class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negs = 0

        for r in grid:
            for c in r:
                if c < 0:
                    negs += 1
        return negs