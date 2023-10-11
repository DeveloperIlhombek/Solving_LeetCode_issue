class Solution:
    def intersection(self, nums1: list[int], nums2:list[int]) -> list[int]:
        res=[]
        x,y=len(nums1),len(nums2)
        maxlen=nums1 if x>=y else nums2
        minlen=nums2 if x>=y else nums1
        for i in minlen:
            if i in maxlen and i not in res:
                res.append(i)
        return res


print(Solution.intersection(Solution,[1,2,2,1],[2,2]))
