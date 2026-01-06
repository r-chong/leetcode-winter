from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        # why do we do this?
        q = deque([root])
        lvl_sums = []

        while q:
            level_size = len(q)

            lvl_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                lvl_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl_sums.append(lvl_sum)
        
        max = float("-inf")
        max_i = 0
        for i, s in enumerate(lvl_sums):
            if s > max:
                max = s
                max_i = i + 1
        
        return max_i

# divergences:
# must sum node at POP time not iterate over array q
# per-level logic lives below the while and above the for
# enumerate returns index, value not value, index