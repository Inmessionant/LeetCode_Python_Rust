#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result = {-1, -1};

        if (nums.size() == 0) {
            return result;
        }

        int left = 0;
        int right = nums.size() - 1;
        int mid;


        while (left < right) {
            mid = left + (right - left) / 2;
            if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        if (nums[left] == target) {
            result[0] = left;
        } else {
            return result;
        }

        left = 0;
        right = nums.size() - 1;

        while (left < right) {
            mid = left + (right - left + 1) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }

        if (nums[right] == target) {
            result[1] = right;
        }

        return result;
    }
};

int main() {
    int target = 8;
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    vector<int> result = Solution().searchRange(nums, target);
    for (int res: result) {
        cout << "result: " << res << endl;
    }

    return 0;
}