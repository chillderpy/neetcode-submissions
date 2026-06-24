class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = [0] * len(nums)
        for idx in range(len(nums)):
            if idx != 0:
                if nums[idx] == nums[idx-1] + 1:
                    res[idx] = res[idx-1] + 1
                elif nums[idx] == nums[idx-1]:
                    res[idx] = res[idx-1]
                else:
                    res[idx] = 1
            else:
                res[idx] = 1
        
        return max(res)