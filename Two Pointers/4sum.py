class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4: 
            return []
        nums.sort()
        answer = []
        seen = set()
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] == target:
                        if (nums[i], nums[j], nums[left], nums[right]) not in seen:
                            answer.append([nums[i], nums[j], nums[left], nums[right]])
                            seen.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

        return answer