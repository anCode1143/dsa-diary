/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::queue<std::tuple<TreeNode*, int>> q;
        q.push({root, 0});
        std::queue<std::tuple<TreeNode*, int>> previous;
        while (!q.empty()) {
            int level_size = q.size();
            previous = q;
            for (int i = 0; i < level_size; i++) {
                std::tuple<TreeNode*, int> parent_tuple = q.front();
                q.pop();
                auto [parent, pos] = parent_tuple;
                if (parent->left != nullptr) {
                    q.push({parent->left, pos-1});
                }
                if (parent->right != nullptr) {
                    q.push({parent->right, pos+1});
                }
            }
        }
        std::tuple<TreeNode*, int> answer = previous.front();
        return std::get<0>(answer)->val;
    }
};