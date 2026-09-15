class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0 for _ in range(len(nums1))]
        for val in nums2:
            prevMax = 0
            for candidateIdx in range(len(nums1)):
                original = dp[candidateIdx]
                if val == nums1[candidateIdx]:
                    dp[candidateIdx] = max(dp[candidateIdx], prevMax+1)
                prevMax = max(prevMax, original)
        return max(dp)