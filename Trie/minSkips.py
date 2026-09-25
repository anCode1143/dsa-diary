from functools import cache

class Solution:
    class TrieNode:
        def __init__(self):
            self.isWord = False
            self.next = [None] * 26

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = self.TrieNode()
        for word in dictionary:
            curr = root
            for char in word:
                if not curr.next[ord(char) - ord("a")]:
                    curr.next[ord(char) - ord("a")] = self.TrieNode()
                curr = curr.next[ord(char) - ord("a")]
            curr.isWord = True

        @cache
        def dp(i):
            if i == len(s):
                return 0
            best = 1 + dp(i + 1) 
            node = root
            for j in range(i, len(s)):
                node = node.next[ord(s[j]) - ord("a")]
                if not node:
                    break       
                if node.isWord:
                    best = min(best, dp(j + 1))
            return best

        return dp(0)