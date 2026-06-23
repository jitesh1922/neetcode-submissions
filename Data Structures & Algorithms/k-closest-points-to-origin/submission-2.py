import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i,j):
            return math.sqrt(i**2 + j**2)
        
        minHeap = []
        for i,j in points:
            minHeap.append([distance(i,j), i,j])
        
        #minHeap.sort(key=lambda x: x[0])
        #print(minHeap)
        heapq.heapify(minHeap)
        ans = []
        while k:
            _,x,y = heapq.heappop(minHeap)
            ans.append([x,y])
            k -= 1

        return ans