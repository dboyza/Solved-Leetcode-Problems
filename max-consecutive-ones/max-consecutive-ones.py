class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0
        max_count = 0
        
        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                curr_count = 0
            max_count = max(max_count, curr_count)
                
        return max_count