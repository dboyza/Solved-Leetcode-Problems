class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        check = set()
        
        for num in nums1:
            check.add(num)
            
        for num in nums2:
            if num in check:
                intersection.append(num)
                check.remove(num)
                
        return intersection