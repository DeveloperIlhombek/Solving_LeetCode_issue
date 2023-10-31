class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        sortArr=sorted(nums)
        revArr=sorted(nums,reverse=True)
        if nums==sortArr or nums == revArr:
            return True
        else:
            return False

print(Solution.isMonotonic(Solution,[1,3,2]))