class Solution {
public:
    string predictPartyVictory(string senate) {
        int radiant = 0;
        int dire = 0;
        int n = senate.size();
        for (int pos = 0; pos < n; pos++) {
            if (senate[pos] == 'R') radiant++;
            else dire++;
        }

        while (radiant && dire) {
            for (int i = 0; i < n; i++) {
                if (senate[i] == 'R') {
                    if (dire == 0) break;
                    senate = ban_next('D', i, senate);
                    dire--;
                }
                else if (senate[i] == 'D') {
                    if (radiant == 0) break;
                    senate = ban_next('R', i, senate);
                    radiant--;
                }
            }
        }

        return radiant ? "Radiant" : "Dire";
    }

    string ban_next(char ban, int start, string senate) {
        int n = senate.size();
        int i = (start + 1) % n;
        while (i != start) {
            if (senate[i] == ban) {
                senate[i] = '.';
                return senate;
            }
            i = (i + 1) % n;
        }
        return senate;
    }
};