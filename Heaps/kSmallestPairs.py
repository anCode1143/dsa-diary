import heapq
from typing import List

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = [(nums1[0] + nums2[0], 0, 0)]
    answer = []
    seen = set()
    while len(answer) < k:
        _, idxOne, idxTwo = heapq.heappop(heap)
        answer.append((nums1[idxOne], nums2[idxTwo]))
        if idxOne + 1 < len(nums1) and (idxOne+1, idxTwo) not in seen:
            heapq.heappush(heap, (nums1[idxOne+1] + nums2[idxTwo], idxOne+1, idxTwo))
            seen.add((idxOne+1, idxTwo))
        if idxTwo + 1 < len(nums2) and (idxOne, idxTwo+1) not in seen:
            heapq.heappush(heap, (nums1[idxOne] + nums2[idxTwo+1], idxOne, idxTwo+1))
            seen.add((idxOne, idxTwo+1))
    return answer

print(kSmallestPairs([1,7,11], [2,4,6], 3))