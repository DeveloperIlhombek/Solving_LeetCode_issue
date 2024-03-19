class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (time // (n-1)) % 2 ==0:
            return [i for i in range(1,n+1)][time % (n-1)]
        return [i for i in range(1,n+1)][::-1][time % (n-1)]


print(Solution.passThePillow(Solution,4,5))
