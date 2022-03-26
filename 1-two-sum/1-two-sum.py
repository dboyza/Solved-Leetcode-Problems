class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        
        for i, num in enumerate(nums):
            if num in difference:
                return [difference[num], i]
            difference[target-num] = i
            