class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        if (accumulate(matchsticks.begin(), matchsticks.end(), 0) % 4) return false;
        vector<int> bucket = {0, 0, 0, 0};
        return backtracking(matchsticks, 0, bucket);
    }

    bool backtracking(vector<int>& matchsticks, int index, vector<int>& bucket) {
        if (index == matchsticks.size()) {
            if (bucket[0] == bucket[1] && bucket[1] == bucket[2] && bucket[2] == bucket[3]) return true;
            else return false;
        }
        int target = accumulate(matchsticks.begin(), matchsticks.end(), 0) / 4;
        for (int idx = 0; idx < 4; idx++) {
            if (idx > 0 && bucket[idx] == bucket[idx-1]) continue;
            if (bucket[idx] + matchsticks[index] > target) continue;
            bucket[idx] += matchsticks[index];
            if (backtracking(matchsticks, index+1, bucket)) return true;
            bucket[idx] -= matchsticks[index];
        }
        return false;
    }
};