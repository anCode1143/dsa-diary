from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answer = []
        wordDict = set(wordDict)
        def backtrack(start, end, s):
            if end == len(s):
                return
            word = s[start:end+1]
            if word in wordDict:
                if end == len(s)-1:
                    answer.append(s)
                    return
                else:
                    backtrack(end+2, end+2, s[:end+1] + " " + s[end+1:])
            backtrack(start, end+1, s)
        backtrack(0, 0, s)
        return answer