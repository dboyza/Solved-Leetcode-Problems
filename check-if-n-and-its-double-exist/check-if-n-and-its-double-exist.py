class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j and arr[j]*2 == arr[i]:
                    return True
        return False