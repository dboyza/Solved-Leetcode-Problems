class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        
        for i in range(len(s)-1):
            if r[s[i]] < r[s[i+1]]:
                num -= r[s[i]]
            else:
                num += r[s[i]]
        num += r[s[-1]]
        return num