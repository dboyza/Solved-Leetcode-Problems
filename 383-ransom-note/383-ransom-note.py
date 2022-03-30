class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        note_count = {}
        
        for char in magazine:
            magazine_count[char] = 1 + magazine_count.get(char, 0)
        
        for char in ransomNote:
            note_count[char] = 1 + note_count.get(char, 0)
            
        for key in note_count:
            if key not in magazine_count or magazine_count[key] < note_count[key]:
                return False
            
        return True