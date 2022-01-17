class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = i
        return False
        """
        hashset = set(nums)
        if len(hashset) < len(nums):
            return True
        return False
        