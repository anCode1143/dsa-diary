class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int N = grid.size();
        pair<int,int> island {-1, -1};
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (grid[row][col] == 1) {
                    island = {row, col};
                    break;
                }
            }
            if (island.first != -1) break;
        }
        grid[island.first][island.second] = 2;

        queue<pair<int,int>> island_bfs;
        island_bfs.push(island);
        queue<tuple<int,int,int>> waters;
        while (!island_bfs.empty()) {
            pair<int,int> cell = island_bfs.front();
            island_bfs.pop();
            handle_coast(cell, grid, waters);
            vector<pair<int,int>> candidates = {{cell.first+1, cell.second}, {cell.first-1, cell.second}, 
            {cell.first, cell.second+1}, {cell.first, cell.second-1}};
            for (int i = 0; i < 4; i++) {
                if (is_in_bound(candidates[i], grid) && grid[candidates[i].first][candidates[i].second] == 1) {
                    grid[candidates[i].first][candidates[i].second] = 2;
                    island_bfs.push(candidates[i]);
                }
            }
        }

        while (!waters.empty()) {
            tuple<int,int,int> cell = waters.front();
            waters.pop();
            vector<pair<int,int>> candidates = {{get<0>(cell)+1, get<1>(cell)}, {get<0>(cell)-1, get<1>(cell)}, 
            {get<0>(cell), get<1>(cell)+1}, {get<0>(cell), get<1>(cell)-1}};
            for (int i = 0; i < 4; i++) {
                if (is_in_bound(candidates[i], grid) && grid[candidates[i].first][candidates[i].second] == 1) {
                    return get<2>(cell);
                }
                if (is_in_bound(candidates[i], grid) && grid[candidates[i].first][candidates[i].second] == 0) {
                    grid[candidates[i].first][candidates[i].second] = 2;
                    waters.push({candidates[i].first, candidates[i].second, get<2>(cell)+1});
                }
            }
        }

        return -1;
    }
    void handle_coast(pair<int,int> cell, vector<vector<int>>& grid, queue<tuple<int,int,int>>& waters) {
        vector<pair<int,int>> candidates = {{cell.first+1, cell.second}, {cell.first-1, cell.second}, 
        {cell.first, cell.second+1}, {cell.first, cell.second-1}};
        for (int i = 0; i < 4; i++) {
            if (is_in_bound(candidates[i], grid) && grid[candidates[i].first][candidates[i].second] == 0) {
                grid[candidates[i].first][candidates[i].second] = 2;
                waters.push({candidates[i].first, candidates[i].second, 1});
            }
        }
    }
    bool is_in_bound(pair<int,int> cell, vector<vector<int>>& grid) {
        int N = grid.size();
        return (0 <= cell.first && cell.first < N && 0 <= cell.second && cell.second < N);
    }
};
