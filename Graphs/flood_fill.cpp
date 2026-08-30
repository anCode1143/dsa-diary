class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;
        dfs(image, sr, sc, color, image[sr][sc]);
        return image;
    }

    void dfs(vector<vector<int>>& image, int row, int col, int color, int target) {
        image[row][col] = color;
        vector<vector<int>> paths = {
        {row+1, col},
        {row-1, col},
        {row, col+1},
        {row, col-1}
        };
        for (int i = 0; i < 4; i++) {
            if (isValid(image, paths[i][0], paths[i][1]) && image[paths[i][0]][paths[i][1]] == target) {
                dfs(image, paths[i][0], paths[i][1], color, target);
            }
        }
    }

    bool isValid(vector<vector<int>>& image, int row, int col) {
        return (0 <= row && row < image.size() && 0 <= col && col < image[0].size());
    }
};