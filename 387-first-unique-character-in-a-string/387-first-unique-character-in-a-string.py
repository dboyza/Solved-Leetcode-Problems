class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        occur = {}
        
        for char in s:
            if char in occur:
                occur[char] += 1
            else:
                occur[char] = 1
        
        for i in range(len(s)):
            if occur[s[i]] == 1:
                return i
            
        return -1