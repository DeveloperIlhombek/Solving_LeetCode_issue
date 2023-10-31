class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1: return 1
        ans=0
        for i in range(x):
            if i*i<=x:
                ans=i
            else:
                break
        return ans


print(Solution.mySqrt(Solution,17))