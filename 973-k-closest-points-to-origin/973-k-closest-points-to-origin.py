import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Create a minHeap
        minHeap = []
        results = []
        #iterate through whole list
        for point in points:
            #add to min heap
            heapq.heappush(minHeap, [sqrt((point[0]**2)+(point[1]**2)),point])    
            #pop K number of times/ or while heap is empty
        for _ in range(k):
            results.append(heapq.heappop(minHeap)[1])
        return results
        