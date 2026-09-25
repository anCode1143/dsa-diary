class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intervalOne = 0
        intervalTwo = 0
        answer = []
        while intervalOne < len(firstList) and intervalTwo < len(secondList):
            start = max(firstList[intervalOne][0], secondList[intervalTwo][0])
            end = min(firstList[intervalOne][1], secondList[intervalTwo][1])
            if start <= end:
                answer.append([start, end])
            if firstList[intervalOne][1] > secondList[intervalTwo][1]:
                intervalTwo += 1
            else:
                intervalOne += 1
        return answer