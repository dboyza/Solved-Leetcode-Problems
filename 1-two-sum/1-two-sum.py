class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        
        Time: O(n^2), Space: O(1)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
        """
        
        
        """
        Time: O(n), Space: O(n)
        Use a hashmap (dictionary)
        Add each element of nums to the dictionary with (key=target-nums[i], value=i)
        """
        seen = {}
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            else:
                seen[target-nums[i]] = i