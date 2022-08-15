class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        # pass 1
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        # pass 2
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans
        