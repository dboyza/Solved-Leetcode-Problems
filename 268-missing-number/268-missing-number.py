class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if count != nums[i]:
                return count
            count += 1
        return len(nums)
            