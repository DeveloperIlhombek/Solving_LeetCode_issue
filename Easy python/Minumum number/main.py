class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        ans = [0]
        for i in nums:
            ans += [ans[-1] + i]
        a = []
        for i in range(1, len(ans)):
            a += [abs(ans[-1] - ans[i] - ans[i - 1])]
        return a

print(Solution.leftRigthDifference(Solution,[10,4,7,3]))
