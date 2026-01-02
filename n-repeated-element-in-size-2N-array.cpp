class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        // create frequency array in O(n), and when we increment to n, return that i
        size_t n = nums.size() / 2;
        std::vector<int> freq(1e4, 0);

        for (int i = 0; i < nums.size(); ++i) {
            ++freq[nums[i]];

            if (freq[nums[i]] == n) {
                return nums[i];
            }
        }

        // should never get here as per problem spec
        return 0;
    }
};

// divergences:
// at first I created n + 1 elements, not 1e4
// indexed freq by i not nums[i]
// no need for nums.size() - 1