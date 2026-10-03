class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        answer = sum(cardPoints[len(cardPoints) - k:])
        curr = answer
        right = 0
        for i in range(k):
            right += cardPoints[i]
            curr -= cardPoints[len(cardPoints) - k + i]
            answer = max(answer, right + curr)
        return answer