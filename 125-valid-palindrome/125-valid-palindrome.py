class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """ NEW STRING METHOD
        
        new_s = ""
        
        for char in s:
            if char.isalpha() or char.isdigit():
                new_s += char.lower()
                    
        return new_s == new_s[::-1]
        
        """
        
        # TWO POINTER METHOD
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
        