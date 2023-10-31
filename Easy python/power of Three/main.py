class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n in [3 ** x for x in range(20)]
print(Solution.isPowerOfThree(Solution,1))



