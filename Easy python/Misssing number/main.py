class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        maxnumber=max(nums)
        if maxnumber >= len(nums):
            listnumber=range(len(nums))
            for i in listnumber:
                if i not in nums:
                    return i
                else:continue
        else:
            return len(nums)

print(Solution.missingNumber(Solution, nums = [0,1]))

