class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set(nums)
        
        return len(_set) != len(nums)
            