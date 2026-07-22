class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def anagram(a):
            letter_dict = {}
            for letter in a:
                letter_dict[letter] = letter_dict.get(letter, 0) + 1
            return letter_dict
        
        if anagram(s) == anagram(t):
            return True
        else: 
            return False
                