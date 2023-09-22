class Solution:
    def twoSum(self, nums,target) ->list[int]:
        length=len(nums)
        for i in range(length):
            for j in range(length):
                if i==j:
                    continue
                CurrentSum=nums[i]+nums[j]
                if CurrentSum==target:
                    return [i,j]




