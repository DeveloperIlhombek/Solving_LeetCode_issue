class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)

print(Solution.searchInsert(Solution,[1,3,5,6],5))