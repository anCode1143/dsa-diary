class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # binary search for max of minPartitionSum
        # run feasability check for each guess
        def canPartition(sum):
            currSum = 0
            partitions = 1
            for num in nums:
                currSum += num
                if currSum > sum:
                    currSum = num
                    partitions += 1
            return partitions <= k

        left = max(nums)
        right = sum(nums)
        answer = right
        while left < right:
            middle = ((right - left) // 2) + left
            if canPartition(middle):
                answer = middle
                right = middle
            else: left = middle + 1
        return answer