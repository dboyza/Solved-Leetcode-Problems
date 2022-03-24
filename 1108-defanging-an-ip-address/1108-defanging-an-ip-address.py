class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_addr = ""
        
        for char in address:
            if char == '.':
                new_addr += "[.]"
            else:
                new_addr += char
                
        return new_addr