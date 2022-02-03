class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = ((end-start)//2)+start
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid-1
            elif target > nums[mid]:
                start = mid+1
        return -1