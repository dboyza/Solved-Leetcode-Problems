class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = min(nums)
        curr_sum = 0
        
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            largest = max(largest, curr_sum)
                
        return max(largest, curr_sum)