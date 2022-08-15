import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        res = []
        heapq.heapify(heap)
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for key in count:
            heapq.heappush(heap, (-count[key], key))
            
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res