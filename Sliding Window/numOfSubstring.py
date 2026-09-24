class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {"a":0, "b":0, "c":0}
        answer = 0
        right = 0
        left = 0
        while right < len(s):
            freq[s[right]] += 1
            while freq["a"] and freq["b"] and freq["c"]:
                freq[s[left]] -= 1
                left += 1
            answer += left
            right += 1
        return answer
