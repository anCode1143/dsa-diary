class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        vector<int> dp(books.size()+1, INT_MAX);
        dp[0] = 0;
        for (int new_book = 1; new_book <= books.size(); new_book++) {
            int width = 0;
            int height = 0;
            for (int divide = new_book; divide > 0; divide--) {
                width += books[divide-1][0];
                if (width > shelfWidth) break;
                height = max(height, books[divide-1][1]);
                dp[new_book] = min(dp[new_book], dp[divide-1] + height);
            }
        }
        return dp[books.size()];
    }
};