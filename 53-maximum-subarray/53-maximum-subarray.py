class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        
        for i in range(0, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            
        return max_sum