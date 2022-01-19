class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {")":"(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in mydict:
                if stack == [] or stack.pop() != mydict[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0