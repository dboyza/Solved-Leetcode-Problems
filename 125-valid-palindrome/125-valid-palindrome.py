class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        for char in s:
            if char.isalpha() or char.isdigit():
                new_s += char.lower()
                    
        return new_s == new_s[::-1]
        
        