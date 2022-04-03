class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_a = {}
        counts_b = {}
        
        for char in s:
            counts_a[char] = 1 + counts_a.get(char, 0)
            
        for char in t:
            counts_b[char] = 1 + counts_b.get(char, 0)
        
        for key in counts_a:
            if key not in counts_b or counts_a[key] != counts_b[key]:
                return False
            
        return True