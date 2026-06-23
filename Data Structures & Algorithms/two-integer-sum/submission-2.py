class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i,j in enumerate(nums):
            map[j] = i

        for i,j in enumerate(nums):
            diff= target - j

            if diff in map and map[diff] != i:
                
                return  [i, map[diff]]
        
        return []
            