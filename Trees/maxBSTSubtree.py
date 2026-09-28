# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode | None) -> int:
        answer = 0

        def postOrder(node):
            nonlocal answer
            if not node:
                return (0, float('inf'), float('-inf'))
            leftBst, leftMin, leftMax = postOrder(node.left)
            rightBst, rightMin, rightMax = postOrder(node.right)

            if leftBst < 0 or rightBst < 0 or not leftMax < node.val < rightMin:
                return (-1, 0, 0)

            size = leftBst + rightBst + 1
            answer = max(answer, size)
            return (size, min(node.val, leftMin), max(node.val, rightMax))

        postOrder(root)
        return answer