class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        length = len_i = len(nums)
        i = 0
        
        while i < length:
            if nums[i] == val:
                count += 1
                del nums[i]
                length -= 1
            else:
                i += 1
                
        return len_i-count