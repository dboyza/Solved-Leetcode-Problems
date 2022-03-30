class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        note_count = {}
        
        for char in magazine:
            magazine_count[char] = 1 + magazine_count.get(char, 0)
        
        for char in ransomNote:
            if char not in magazine_count or magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1
            
        return True