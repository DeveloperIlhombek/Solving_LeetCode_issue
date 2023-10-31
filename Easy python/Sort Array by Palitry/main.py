class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res,res2=[],[]
        for i in nums:
            res.append(i) if i%2==0 else res2.append(i)
        for i in range(len(res2)):
            res.append(res2[i])
        return res
print(Solution.sortArrayByParity(Solution,[0]))

