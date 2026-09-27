# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        colRow = defaultdict(lambda: defaultdict(SortedList))
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, col = queue.popleft()
            colRow[col][row].add(node.val)
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        answer = []
        minCol = min(colRow.keys())
        maxCol = max(colRow.keys())
        for col in range(minCol, maxCol+1):
            if col in colRow:
                colMap = colRow[col]
                minKey = min(colMap.keys())
                maxKey = max(colMap.keys())
                answerCol = []
                for row in range(minKey, maxKey+1):
                    if row in colMap:
                        answerCol += list(colMap[row])
                answer.append(answerCol)
        return answer