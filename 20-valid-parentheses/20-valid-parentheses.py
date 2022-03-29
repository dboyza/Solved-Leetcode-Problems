class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')':'(', '}': '{', ']': '['}
        
        for char in s:
            if char in check:
                if stack == [] or stack.pop() != check[char]:
                    return False
            else:
                stack.append(char)
                
        return stack == []