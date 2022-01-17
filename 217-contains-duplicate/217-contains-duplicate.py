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
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        return False
        