import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i,j):
            return math.sqrt(i**2 + j**2)
        
        minHeap = []
        for i,j in points:
            minHeap.append((distance(i,j), i,j))
        
        minHeap.sort(key=lambda x: x[0])
        #print(minHeap)
        ans = []
        for i in range(k):
            ans.append([minHeap[i][1], minHeap[i][2]])

        return ans