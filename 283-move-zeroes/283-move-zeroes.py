class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        length = len(nums)
        
        while i < length:
            if nums[i] == 0:
                del nums[i]
                length -= 1
                count += 1
            else:
                i += 1
                
        for _ in range(count):
            nums.append(0)
        
        return nums