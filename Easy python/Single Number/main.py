class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            x=nums.count(i)
            if x == 1:
                return i




print(Solution.singleNumber(Solution,[2,2,1]))

