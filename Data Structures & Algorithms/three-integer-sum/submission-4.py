class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        seen = set()
        res = []
        for idx in range(len(nums)):
            l = idx + 1
            r = n
            target = -nums[idx]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    if (nums[l], nums[r], nums[idx]) not in seen:
                        res.append([nums[l], nums[r], nums[idx]])
                        seen.add((nums[l], nums[r], nums[idx]))
                    l += 1
                    r -=1
        
        return res