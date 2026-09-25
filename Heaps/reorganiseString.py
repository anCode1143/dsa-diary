class Solution:
    def reorganizeString(self, s: str) -> str:
        charOccur = defaultdict(int)
        for char in s:
            charOccur[char] += 1
        heap = []
        for char, freq in charOccur.items():
            heap.append((-freq, char))
            if freq > (len(s) + 1) // 2:
                return ""
        
        heapq.heapify(heap)
        answer = []
        buffer = ()
        while heap:
            freq, char = heapq.heappop(heap)
            answer.append(char)
            if buffer and buffer[0] < 0:
                heapq.heappush(heap, buffer)
            buffer = (freq+1, char)
        return "".join(answer)