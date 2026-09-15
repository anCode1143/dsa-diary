class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums):
            if (0 < nums[pointer] <= len(nums) and not nums[pointer] == pointer + 1
            and not nums[pointer] == nums[nums[pointer] - 1]):
                store = nums[pointer]
                nums[pointer] = nums[nums[pointer] - 1]
                nums[store - 1] = store
            else:
                pointer += 1
        for index in range(len(nums)):
            if not index + 1 == nums[index]:
                return index + 1
        return len(nums) + 1

