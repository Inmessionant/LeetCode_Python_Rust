#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) { // versin 1 [left, right]
        int left = 0;
        int right = nums.size() - 1;
        int mid;

        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    int search2(vector<int>& nums, int target) { // version 2 [left, right)
        int left = 0;
        int right = nums.size() - 1;
        int mid;

        while (left < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        if (nums[left] == target) {
            return left;
        }

        return -1;
    }
};

int main() {
    int target = 4;
    vector<int> nums = {1, 2, 3 ,4};
    cout << "result idx: " << Solution().search(nums, target) << endl;
    cout << "result idx: " << Solution().search2(nums, target) << endl;
    return 0;
}