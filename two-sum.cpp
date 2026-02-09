class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); ++i) {
            if (seen.find(target - nums[i]) != seen.end()) {
                return {i, seen[target - nums[i]]};
            } else {
                seen[nums[i]] = i;
            }
        }
        return {};
    }
};