class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result=[]
        freq=nums[::2]
        val=nums[1::2]
        for i in range(len(freq)):
            while freq[i]>0:
                result.append(val[i])
                freq[i]-=1
        return result

print(Solution.decompressRLElist(Solution, [1,1,2,3]))






#         Input: nums = [1,2,3,4]
#         Output: [2,4,4,4]
