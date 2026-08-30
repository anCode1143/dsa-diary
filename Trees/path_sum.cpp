class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) {
            return false;
        }
        return travserse(root, targetSum, 0);
    }
    bool travserse(TreeNode* root, int targetSum, int currSum) {
        currSum += root->val;
        if (currSum == targetSum && root->left == nullptr && root->right == nullptr) {
            return true;
        }
        if (root->left != nullptr) {
            if (travserse(root->left, targetSum, currSum)) {
                return true;
            }
        }
        if (root->right != nullptr) {
            if (travserse(root->right, targetSum, currSum)) {
                return true;
            }
        }
        return false;
    }
};