class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
            
        if s_map.keys() != t_map.keys():
            return False
        
        for key in s_map:
            if key in t_map and t_map[key] != s_map[key]:
                return False
            
        return True