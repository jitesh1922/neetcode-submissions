class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minimum = 1005

        start =0
        end = len(nums)-1
        while start <= end:
            mid = (end + start) // 2

            minimum = min(minimum, nums[mid])

            if nums[mid] > nums[end]:
                start = mid +1

            else:
                end = mid -1
        
        return minimum
        