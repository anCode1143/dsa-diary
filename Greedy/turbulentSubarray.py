class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if len(set(arr)) == 1:
            return 1
        if len(arr) < 3:
            return len(arr)
        maxCount = 0
        currCount = 1
        for ptr in range(2, len(arr)):
            if arr[ptr-2] > arr[ptr-1] < arr[ptr] or arr[ptr-2] < arr[ptr-1] > arr[ptr]:
                currCount += 1
            else: 
                currCount = 1
            maxCount = max(maxCount, currCount)
        return maxCount + 1