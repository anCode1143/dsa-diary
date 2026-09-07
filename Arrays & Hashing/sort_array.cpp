class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        return merge_sort(nums);
    }

    vector<int> merge_sort(vector<int>& nums) {
        if (nums.size() == 2 && nums[1] < nums[0]) {
            int big = nums[0];
            nums[0] = nums[1];
            nums[1] = big;
        }
        if (nums.size() <= 2) return nums;
        std::vector<int>::iterator mid = nums.begin() + nums.size() / 2;
        std::vector<int> first_half(nums.begin(), mid);
        std::vector<int> second_half(mid, nums.end());
        first_half = merge_sort(first_half);
        second_half = merge_sort(second_half);
        std::vector<int> sorted;
        int s_i = 0;
        int f_i = 0;
        while (s_i < second_half.size() && f_i < first_half.size()) {
            if (second_half[s_i] < first_half[f_i]) {
                sorted.push_back(second_half[s_i]);
                s_i++;
            }
            else {
                sorted.push_back(first_half[f_i]);
                f_i++;
            }
        }
        if (s_i == second_half.size()) {
            sorted.insert(sorted.end(), first_half.begin() + f_i, first_half.end());
        }
        else {
            sorted.insert(sorted.end(), second_half.begin() + s_i, second_half.end());
        }
        return sorted;
    }
};