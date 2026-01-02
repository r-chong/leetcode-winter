class Solution {
public:
    int search(vector<int>& nums, int target) {
        return this->BinarySearch(nums, 0, nums.size() - 1, target);
    }

    int BinarySearch(vector<int>&arr, int left, int right, int target) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return this->BinarySearch(arr, mid + 1, right, target);
        } else {
            return this->BinarySearch(arr, left, mid - 1, target);
        }
    }
};

// divergences:
// mixed up directions again