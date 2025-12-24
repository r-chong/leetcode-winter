class Solution {
    std::unordered_map<int, int> visited;

public:
    int climbStairs(int n) {
        if (n < 0) {
            return 0;
        } else if (n == 0) {
            return 1;
        } else if (this->visited.contains(n)) {   
            return this->visited[n];
        } else {
            this->visited[n] = this->climbStairs(n - 1) + this->climbStairs(n - 2);
            return this->visited[n];
        }
    }
};