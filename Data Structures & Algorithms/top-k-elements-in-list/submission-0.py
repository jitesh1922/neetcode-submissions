class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = []
        for item, freq in count.items():
            max_heap.append((-freq, item))
        
        heapq.heapify(max_heap)
        res = []
        while k:
            val = heapq.heappop(max_heap)
            res.append(val[1])
            k -=1
        
        return res
