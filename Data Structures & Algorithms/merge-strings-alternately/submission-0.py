class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        length = max(len(word1), len(word2))

        for i in range(0, length):
            while i < len(word1):
                merged.append(word1[i])
                break
            while i < len(word2):
                merged.append(word2[i])
                break
        
        return ''.join(merged)