class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        for (int idx = 1; idx < words.size(); idx++) {
            if (!(isFirst(words[idx - 1], words[idx], order))) {
                return false;
            }
        }
        return true;
    }
    
    bool isFirst(string first, string second, string order) {
        int unique_index = 0;
        while (first[unique_index] == second[unique_index]) {
            unique_index++;
            if (unique_index == first.size()) {
                return true;
            }
            else if (unique_index == second.size()) {
                return false;
            }
        }
        size_t first_pos = order.find(first[unique_index]);
        size_t second_pos = order.find(second[unique_index]);
        return first_pos < second_pos;
    }
};