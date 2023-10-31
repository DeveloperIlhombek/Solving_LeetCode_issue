class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        result=[]
        for i in nums:
            if i != val:
                result.append(i)
        return result

print(Solution.removeElement(Solution,[0,1,2,2,3,0,4,2],2))
