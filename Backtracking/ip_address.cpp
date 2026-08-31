class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
       vector<string> answer;
       backtrack(s, 0, answer);
       return answer;
    }

    void backtrack(string curr, int dots, vector<string>& answer) {
        if (dots == 3) {
            string lastNum = curr.substr(curr.rfind('.') + 1);
            if (isValid(lastNum)) answer.push_back(curr);
            return;
        }
        size_t latest = curr.rfind('.');
        size_t segStart = (latest == string::npos) ? 0 : latest + 1;
        int start = segStart + 1;
        while (start < curr.length() && start <= segStart + 3) {
            if (isValid(curr.substr(segStart, start - segStart))) {
                string candidate = curr;
                candidate.insert(start, 1, '.');
                backtrack(candidate, dots + 1, answer);
            }
            start++;
        }
    }

    bool isValid(string s) {
        if (s.empty() || s.length() > 3) return false;
        if (s[0] == '0' && s.length() > 1) return false;
        int num = stoi(s);
        return (num < 256);
    }
};