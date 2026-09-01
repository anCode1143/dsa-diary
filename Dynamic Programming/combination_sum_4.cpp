class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target + 1);
        dp[0] = 1;
        for (int i_target = 1; i_target <= target; i_target++) {
            for (int num_idx = 0; num_idx < nums.size(); num_idx++) {
                if (i_target - nums[num_idx] >= 0) {
                    dp[i_target] += dp[i_target - nums[num_idx]];
                }
            }
        }
        return (int) dp[target];
    }
};