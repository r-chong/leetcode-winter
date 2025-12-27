class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_pre = 0
        y_post = 0

        # process j = 0
        for c in customers:
            if c == 'Y':
                y_post += 1

        # technically the sum of n_pre + y_post but n_pre is 0
        min_cost = y_post 
        earliest_min_idx = 0

        # process j > 0
        for j, c in enumerate(customers):
            if c == 'N':
                n_pre += 1
            else:
                y_post -= 1

            cost = n_pre + y_post

            # note that we're measuring the # of hours passed ("0-indexed") thus the first j is the 0th hour and the 0th index is the 1st hour if that makes sense
            if cost < min_cost:
                min_cost = cost
                earliest_min_idx = j + 1

        return earliest_min_idx