class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # missed these
        n = len(nums1)
        m = len(nums2)
        NEG = float("-inf")

        dp = [[NEG for _ in range(m + 1)] for _ in range(n + 1)]

        i = n - 1
        while i >= 0:
            j = m - 1
            while j >= 0:
                prod = nums1[i] * nums2[j]

                take = prod
                if dp[i + 1][j + 1] != NEG:
                    take = max(take, prod + dp[i + 1][j + 1])

                skip1 = dp[i + 1][j]
                skip2 = dp[i][j + 1]

                dp[i][j] = max(take, skip1, skip2)

                j -= 1
            i -= 1

        return dp[0][0]

# divergences:
# dp array should not have been blank
# instead of while true, use one of the indices
# had take = prod + max(0, dp[i+1][j+1])
# helps to create len variables