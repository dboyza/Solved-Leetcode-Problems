class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_len = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_len += 1
            elif zero_len > 0:
                temp = nums[i]
                nums[i] = 0
                nums[i-zero_len] = temp
                
        return nums