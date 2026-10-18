class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)

        longest = 0 
        for i in nums:
            if i-1 in num:
                continue
            curr_length = 1
            curr_num = i
            while curr_num + 1 in num :
                curr_length += 1
                curr_num += 1
            longest = max( curr_length, longest)
        return longest


"""

2 ->  3, 4 
"""