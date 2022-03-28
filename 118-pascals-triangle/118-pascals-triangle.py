class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for i in range(numRows-1):
            prev = [0] + result[-1] + [0]
            curr = []
            for j in range(len(result[-1])+1):
                curr.append(prev[j] + prev[j+1])
            result.append(curr)
            
        return result