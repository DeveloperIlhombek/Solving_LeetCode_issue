class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)
        return nums
print(Solution.moveZeroes(Solution,[0,1,0,3,12]))




