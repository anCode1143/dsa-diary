class Solution {
public:
    int calculate(string s) {
        s = operate(s, "*/");
        s = operate(s, "+-");
        return stoi(s);
    }

    string operate(const string& s, const string& ops) {
        long long a = 0;
        char curr_op = 0;          // 0 = no pending operator
        string after = "";
        int pointer = 0;

        while (pointer < s.size()) {
            char c = s[pointer];
            if (c == ' ') { pointer++; continue; }

            if (isdigit(c)) {
                int end = pointer;
                while (end < s.size() && isdigit(s[end])) end++;
                long long num = stoll(s.substr(pointer, end - pointer));
                a = (curr_op != 0) ? eval(a, curr_op, num) : num;
                pointer = end;
            } else {
                if (ops.find(c) != string::npos) {
                    curr_op = c;
                } else {
                    after += to_string(a) + c;
                    curr_op = 0;
                }
                pointer++;
            }
        }
        after += to_string(a);
        return after;
    }

    long long eval(long long a, char op, long long b) {
        if (op == '+') return a + b;
        if (op == '-') return a - b;
        if (op == '*') return a * b;
        return a / b;
    }
};