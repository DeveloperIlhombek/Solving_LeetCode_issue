class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        bob=nums[1::2]
        alice=nums[::2]
        number=int(len(nums)/2)
        arr=[]
        for i in range(number):
            arr.append(bob[i])
            arr.append(alice[i])
        return arr
        # for i in range(0,len(nums),2):
        #     nums[i],nums[i+1]=nums[i+1],nums[i]
        # return nums

print(Solution.numberGame(Solution,[1,2,3,4,5,6,7,8]))