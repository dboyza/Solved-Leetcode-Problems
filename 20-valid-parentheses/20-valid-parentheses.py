class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {")":"(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char not in mydict:
                stack.append(char)
            elif stack == [] or stack.pop() != mydict[char]:
                    return False
        return stack == []