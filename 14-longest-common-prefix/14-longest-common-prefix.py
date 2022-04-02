class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        lp = max(strs)
        
        for i in range(1, len(strs)):
            char = 0
            common = ""
            while char < min(len(strs[i-1]), len(strs[i])) and strs[i-1][char] == strs[i][char]:
                common += strs[i][char]
                char += 1
                
            lp = min(lp, common)
        
        return lp