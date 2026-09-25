# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode | None, p: int, q: int) -> int:
        if p == q:
            return 0
        def postOrder(node):
            ans, pDist, qDist = -1, -1, -1
            if node.left:
                ansL, pDistL, qDistL = postOrder(node.left)
                ans = ansL if ansL > -1 else ans
                pDist = pDistL if pDistL > -1 else pDist
                qDist = qDistL if qDistL > -1 else qDist
            if node.right:
                ansR, pDistR, qDistR = postOrder(node.right)
                ans = ansR if ansR > -1 else ans
                pDist = pDistR if pDistR > -1 else pDist
                qDist = qDistR if qDistR > -1 else qDist

            if node.val == p:
                pDist = 0
            if node.val == q:
                qDist = 0

            if ans > -1:
                return (ans, 0, 0)
            if pDist > -1 and qDist > -1:
                return (pDist + qDist, 0, 0)
            elif pDist > -1:
                return (-1, pDist+1, -1)
            elif qDist > -1:
                return (-1, -1, qDist+1)
            else:
                return (-1, -1, -1)
        ans, _, _ = postOrder(root)
        return ans