class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        int a_count = a;
        int b_count = b;
        int c_count = c;
        int* prev = nullptr;
        string answer = "";
        while (!isEnd(a_count, b_count, c_count, prev)) {
            if (prev != &a_count && a_count == max({a_count, b_count, c_count})) {
                answer += (a_count > 1 ? "aa" : "a");
                a_count -= (a_count > 1 ? 2 : 1);
                prev = &a_count;
            }
            else if (prev != &b_count && b_count == max({a_count, b_count, c_count})) {
                answer += (b_count > 1 ? "bb" : "b");
                b_count -= (b_count > 1 ? 2 : 1);
                prev = &b_count;
            }
            else if (prev != &c_count && c_count == max({a_count, b_count, c_count})) {
                answer += (c_count > 1 ? "cc" : "c");
                c_count -= (c_count > 1 ? 2 : 1);
                prev = &c_count;
            }
            else {
                int* second = getSecond(a_count, b_count, c_count, prev);
                (*second)--;
                if (second == &a_count) answer += 'a';
                else if (second == &b_count) answer += 'b';
                else answer += 'c';
                prev = second;
            }
        }
        return answer;
    }

    bool isEnd(int& a, int& b, int& c, int* prev) {
        if (a == 0 && b == 0 && c == 0) {
            return true;
        }
        if (prev == &a) {
            return (b == 0 && c == 0);
        }
        if (prev == &b) {
            return (a == 0 && c == 0);
        }
        if (prev == &c) {
            return (a == 0 && b == 0);
        }
        return false;
    }

    int* getSecond(int& a, int& b, int& c, int* prev) {
    std::array<int*, 3> ptrs = {&a, &b, &c};

    std::sort(ptrs.begin(), ptrs.end(), [prev](int* x, int* y) {
        if (*x != *y) {
            return *x < *y;
        }
        return x == prev;
    });

    return ptrs[1]; 
    }
};
