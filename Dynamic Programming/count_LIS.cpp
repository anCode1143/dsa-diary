class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        vector<int> max_subseq (nums.size(), 1);
        vector<int> max_subsequences (nums.size(), 1);
        for (int i = nums.size() - 1; i >= 0; i--) {
            for (int backstep = i + 1; backstep < nums.size(); backstep++) {
                if (nums[backstep] > nums[i]) {
                    max_subseq[i] = max(max_subseq[i], 1 + max_subseq[backstep]);
                }
            }
            if (!(max_subseq[i] == 1)) {
                max_subsequences[i] = 0;
                for (int backstep = i + 1; backstep < nums.size(); backstep++) {
                    if (nums[backstep] > nums[i] && max_subseq[i] == 1 + max_subseq[backstep]) {
                        max_subsequences[i] += max_subsequences[backstep];
                    }
                }
            }
        }
        int maxLen = *max_element(max_subseq.begin(), max_subseq.end());
        int total = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (max_subseq[i] == maxLen) {
                total += max_subsequences[i];
            }
        }
        return total;
    }
};