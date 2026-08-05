#include <string>
bool validPalindrome(string s) {
    return recursion(s, false);
}

bool recursion(string s, bool delete_used) {
    int left = 0; int right = s.size() - 1;
    while (left < right) {
        if (s[left] == s[right]) {
            left++; right--;
        }
        else if (!delete_used) {
            return recursion(s.substr(left, right - left), true) || recursion(s.substr(left + 1, right - left), true);
        }
        else return false;
    }
    return true;
}