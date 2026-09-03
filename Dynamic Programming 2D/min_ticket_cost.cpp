class Solution {
public:
    vector<int> dp{std::vector<int>(366)};

    int mincostTickets(vector<int>& days, vector<int>& costs) {
        for (int i = 0; i < days.size(); i++) {
            int prev = (i == 0) ? 0 : dp[days[i] - 1];
            int day = costs[0] + prev;
            int week = costs[1] + (days[i] - 7 < 0 ? 0 : dp[max(0, days[i] - 7)]);
            int month = costs[2] + (days[i] - 30 < 0 ? 0 : dp[max(0, days[i] - 30)]);
            int best = min({day, week, month});

            int end = (i == days.size() - 1) ? 366 : days[i + 1];
            fill_dp(days[i], end, best);
        }
        return dp[365];
    }

    void fill_dp(int start, int end, int price) {
        if (start < 0) start = 0;
        fill(dp.begin() + start, dp.begin() + end, price);
    }
};