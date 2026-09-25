class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        answerSet = set()
        answer = [[1, n]]
        pointer = 0
        while pointer < len(answer):
            for idx, factor in enumerate(answer[pointer]):
                seen = set()
                for candidate in range(2, (factor//2)+1):
                    if factor % candidate == 0 and factor // candidate not in seen:
                        new = answer[pointer][:]
                        new[idx] = candidate
                        new.append(factor // candidate)
                        new.sort()
                        if tuple(new) not in answerSet:
                            answerSet.add(tuple(new))
                            if pointer == 0:
                                answer.append(new[1:])
                            else:
                                answer.append(new)
                        seen.add(candidate)
            pointer += 1
        return answer[1:]