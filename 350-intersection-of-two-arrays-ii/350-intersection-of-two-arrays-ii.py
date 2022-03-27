class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        
        check1 = {}
        check2 = {}
        
        for num in nums1:
            if num in check1:
                check1[num] += 1
            else:
                check1[num] = 1
                
        for num in nums2:
            if num in check2:
                check2[num] += 1
            else:
                check2[num] = 1
        
        for key in check1:
            if key in check2:
                for _ in range(min(check1[key], check2[key])):
                    intersection.append(key)
                
        return intersection