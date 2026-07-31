def removeDuplicates(self, nums: List[int]) -> int:
    place_ptr, find_unique_ptr = 0, 1
    while find_unique_ptr < len(nums):
        if nums[place_ptr] < nums[find_unique_ptr]:
            nums[place_ptr + 1] = nums[find_unique_ptr]
            place_ptr += 1
        find_unique_ptr += 1
    place_ptr += 1
    return place_ptr