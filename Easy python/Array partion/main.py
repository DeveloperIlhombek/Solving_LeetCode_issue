class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])

print(Solution.arrayPairSum(Solution,[6,2,6,5,1,2]))