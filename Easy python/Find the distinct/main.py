class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            arr = nums[i + 1::]
            lis = nums[:i + 1:]
            result.append(len(set(lis)) - len(set(arr)))
        return result

obj=Solution()
answer=obj.distinctDifferenceArray([3,2,3,4,2])
print(answer)


# Output: [-2,-1,0,2,3]