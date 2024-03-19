class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # answer=[]
        # flag=2
        # while flag>0:
        #     for i in nums:
        #         answer.append(i)
        #     flag -=1
        return nums+nums

print(Solution.getConcatenation(Solution,[5,4]))