

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid;

        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }

        }

        return left;
    }
};

int main() {
    int target = 4;
    vector<int> nums = {1, 2, 3 ,4};
    cout << "result idx: " << Solution().searchInsert(nums, target) << endl;
    return 0;
}