class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map =  set()
        for i in nums:
            if i not in map:
                map.add(i)
            else:
                return True
        
        return False
       