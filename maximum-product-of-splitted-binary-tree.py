# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_d = float("inf")
        self.max = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        prod = self.sumSubtree(root) # total

        total = self.sumSubtree(root)
        half = total // 2

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            sum = left + right + node.val

            # minimize the delta between half (perfect square)
            if abs(sum - half) < self.min_d:
                self.min_d = abs(sum - half)

                # so this product is closest to the max
                self.max = sum * (total - sum)

            return sum # add back into parent

        dfs(root)

        return self.max % (10**9 + 7)
        
    def sumSubtree(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        return self.sumSubtree(node.left) + self.sumSubtree(node.right) + node.val

# divergences:
# square maximum idea
# minimized the wrong thing (sum * (total - sum))
# calculated total in the loop