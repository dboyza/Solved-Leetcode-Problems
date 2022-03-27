class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        counts1 = collections.Counter(words1)
        counts2 = collections.Counter(words2)
        
        for key in counts1:
            if counts1[key] == 1 and counts2[key] == 1:
                count += 1
                counts2[key] = 0
                
        return count
        
        