# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        def minSwaps(level) -> int:
            visited = [False for _ in range(len(level))]
            swaps = 0
            sortedIdx = sorted(range(len(level)), key= lambda i: level[i])
            for i in range(len(level)):
                cycle = 0
                while not visited[i] and not sortedIdx[i] == i:
                    visited[i] = True
                    cycle += 1
                    i = sortedIdx[i]
                swaps += cycle - 1 if cycle > 0 else 0
            return swaps

        queue = deque([root])
        answer = 0
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            answer += minSwaps(level)
        return answer
                
        # 7, 6, 8, 5
        # 2, 1, 3, 0
        # 5, 6, 7, 8
        # T, F, T, F
        # c = 2, s = 