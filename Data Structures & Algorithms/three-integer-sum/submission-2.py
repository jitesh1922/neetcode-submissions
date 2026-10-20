class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            if nums[k] > 0:
                break
            i = k+1
            j = len(nums) - 1

            while i < j:
                value = nums[k] + nums[j] + nums[i]
                if value == 0:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                       # Skip duplicate second elements
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    # Skip duplicate third elements
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif value > 0:
                    j -= 1
                else:
                    i += 1
        
        return result