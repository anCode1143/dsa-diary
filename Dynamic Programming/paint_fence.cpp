class Solution {
public:
    int numWays(int n, int k) {
        std::vector<int> same(n+1), diff(n+1), ans(n+1);
        same[1] = 0;
        diff[1] = k;
        ans[1] = k;
        int idx = 2;
        while (idx <= n) {
            diff[idx] = ans[idx-1]*(k-1);
            same[idx] = diff[idx-1];
            ans[idx] = same[idx] + diff[idx];
            idx++;
        }
        return ans[n];
        
    }
};