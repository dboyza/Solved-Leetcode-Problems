class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        l = r = longest = 0
        
        while r < len(s):
            table[s[r]] = table.get(s[r], 0) + 1
            
            while table[s[r]] > 1:
                table[s[l]] -= 1
                l += 1
                
            longest = max(longest, r-l+1)    
            r += 1
        
        return longest
            