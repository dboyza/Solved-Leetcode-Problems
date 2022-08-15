class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        
        if len(s) == 1:
            return mapping[s]
        
        last = mapping[s[len(s)-1]]
        ans += last
        
        for i in range(len(s)-2, -1, -1):
            if mapping[s[i]] < last:
                ans -= mapping[s[i]]
            else:
                ans += mapping[s[i]]
                
            last = mapping[s[i]]
            
        return ans