class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-i for i in nums]
        heapq.heapify(maxheap)

        while k>1:
            k -= 1
            heapq.heappop(maxheap)
        
        return  -heapq.heappop(maxheap)