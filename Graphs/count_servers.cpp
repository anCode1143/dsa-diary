class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size();
        vector<int> row_count(ROWS), col_count(COLS);
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (grid[row][col] == 1) {
                    row_count[row]++; col_count[col]++;
                }
            }
        }

        int counter = 0;
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (grid[row][col] == 1 
                && (row_count[row] > 1 || col_count[col] > 1)) {
                    counter++;
                }
            }
        }
        return counter;
    }
};