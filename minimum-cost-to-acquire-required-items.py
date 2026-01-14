class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def total(k):
            return (
                k * costBoth 
                + max(0, need1 - k) * cost1 # need1 - k is negative
                + max(0, need2 - k) * cost2 # need2 - k is negative
            )

        m = min(need1, need2)
        M = max(need1, need2)

        return min(total(0), total(m), total(M))

# divergences:
# was treating as a big conditional solution
# the problem is minimizing three different approaches
# k represents the number of type3 that we buy
# so total(0) means buy zero type3 and thus full ammunts of type1 and type2
# total(m) means to buy need1 of type3 and remainder of type2
# total(M) means to buy need2 of type3 and remainder of type1