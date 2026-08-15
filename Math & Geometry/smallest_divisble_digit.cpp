class Solution {
public:
    int smallestNumber(int n, int t) {
        for (int iterator = n; true; iterator++) {
            int product = 1;
            int separator = iterator;
            while (separator > 0) {
                int digit = separator % 10;
                product *= digit;
                separator /= 10;
            }
            if (product % t == 0) {
                return iterator;
            }
        }
    }
};