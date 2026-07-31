def removeElement(self, nums: List[int], val: int) -> int:
    free_place, iterator = 0, 0
    kCount = 0
    while iterator < len(nums):
        if nums[iterator] != val:
            nums[free_place] = nums[iterator]
            free_place += 1
            kCount += 1
        iterator += 1
    return kCount