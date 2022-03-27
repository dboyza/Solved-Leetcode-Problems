class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        counts = collections.Counter(nums1)
        
        for num in nums2:
            if num in counts:
                intersection.append(num)
                counts.pop(num)
                
        return intersection