class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        cum_sum = [0] * (n + 1) # add 1 as we want an extra value on the left
        rev_suf_min = [nums[-1]] * (n + 1)
        max_score = float('-inf')

        for i in range(1, n + 1):
            cum_sum[i] = cum_sum[i - 1] + nums[i - 1]
            rev_suf_min[n - i] = min(nums[n - i], rev_suf_min[n - i + 1])

        for i in range(1, n):
            max_score = max(cum_sum[i] - rev_suf_min[i], max_score)

        return max_score

# divergences:
# misread suffix
# overcounting indexing - it was just [i] for max score not [i+1] etc