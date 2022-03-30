class Solution:
    def firstUniqChar(self, s: str) -> int:
        occur = {}
        
        for i, char in enumerate(s):
            if char in occur:
                occur[char] = -1
            else:
                occur[char] = i
        
        for key in occur:
            if occur[key] != -1:
                return occur[key]
            
        return -1