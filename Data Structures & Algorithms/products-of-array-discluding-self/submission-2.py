class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1 if any(i != 0 for i in nums) else 0
        zero = False
        count = 0
        for n in nums:
            if n != 0:
                total *= n
            else:
                count += 1
                zero = True
                if count == 2:
                    return [0] * len(nums)
        res = []
        for n in nums:
            if n == 0 and zero:
                res.append(total)
            elif n != 0 and zero:
                res.append(0)
            else:
                res.append(total // n)

        return res