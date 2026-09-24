# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if not root: return 0
        count = 0
        def preorder(sums, node):
            nonlocal count
            for idx, num in enumerate(sums):
                sums[idx] = num + node.val
                if sums[idx] == targetSum:
                    count += 1
            sums.append(node.val)
            if node.val == targetSum:
                count += 1
            if node.left: preorder(copy.deepcopy(sums), node.left)
            if node.right: preorder(copy.deepcopy(sums), node.right)
        preorder([], root)
        return count