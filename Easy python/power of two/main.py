class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in [2**x for x in range(32)]

print(Solution.isPowerOfTwo(Solution,1))


