class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        std::set<int> s(friends.begin(), friends.end());
        std::vector<int> res;
        res.reserve(friends.size());

        for (int f : order) {
            if (s.count(f)) {
                res.emplace_back(f);
            }
        }

        return res;
    }
};