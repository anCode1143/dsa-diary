class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        return isOneEditDistance(s, t, false);
    }
    bool isOneEditDistance(string s, string t, bool changed) {
        int idx = 0;
        while (idx < s.size() && idx < t.size()) {
            if (s[idx] != t[idx]) {
                if (changed) {
                    return false;
                }
                else {
                    if (isOneEditDistance(s.substr(idx), t.substr(idx+1), true)
                    || isOneEditDistance(s.substr(idx+1), t.substr(idx), true)
                    || isOneEditDistance(s.substr(idx+1), t.substr(idx+1), true)) {
                        return true;
                    }
                    else return false;
                }
            }
            idx++;
        }
        if (changed) {
            return s.size() == t.size();
        }
        return (s.size() > t.size() ? s.size() - t.size() == 1 : t.size() - s.size() == 1);
    }
};