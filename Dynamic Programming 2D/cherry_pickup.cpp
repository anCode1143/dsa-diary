class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int N = grid.size();
        vector<int> dp(N * N * N * N, INT_MIN);
        int answer = dfs(0, 0, 0, 0, grid, dp, N);
        return answer == -1 ? 0 : answer;
    }

    int dfs(int r1, int c1, int r2, int c2, vector<vector<int>>& grid, vector<int>& dp, int N) {
        if (r1 >= N || r2 >= N || c1 >= N || c2 >= N || grid[r1][c1] == -1 || grid[r2][c2] == -1) return -1;
        if (r1 == N - 1 && c1 == N - 1) return grid[r1][c1];

        int index = ((r1 * N + c1) * N + r2) * N + c2;
        if (dp[index] != INT_MIN) return dp[index];

        int cherries = grid[r1][c1];
        if (r1 != r2 || c1 != c2) cherries += grid[r2][c2];

        int best_step = max({dfs(r1+1, c1, r2+1, c2, grid, dp, N), dfs(r1+1, c1, r2, c2+1, grid, dp, N),
                              dfs(r1, c1+1, r2+1, c2, grid, dp, N), dfs(r1, c1+1, r2, c2+1, grid, dp, N)});

        if (best_step == -1) {
            dp[index] = -1;
            return -1;
        }
        dp[index] = best_step + cherries;
        return dp[index];
    }
};