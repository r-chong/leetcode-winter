class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 1;
        int max_profit = 0;
        int profit;

        while (right < prices.size()) { 
            if (prices[right] > prices[left]) {
                profit = prices[right] - prices[left];

                if (profit > max_profit) {
                    max_profit = profit;
                }
            } else {
                left = right;
            }
            ++right;
        }

        return max_profit;
    }
};

// divergences:
// no need to keep track of indices
// also no need to keep track of past left,right as that has already been processed
// forgot how to move left. I thought it was
// left = std::min(prices[left]); // ???
// but instead it was an else case