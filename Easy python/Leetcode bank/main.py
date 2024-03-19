class Solution:
    def totalMoney(self, n: int) -> int:
        reminder=n % 7
        summa=(n // 7)*28
        for i in range(7,7*(n // 7),7):
            summa +=i
        for i in range(1,reminder+1):
            summa+=i
        summa +=reminder*(n//7)
        return summa

solution=Solution()
s=solution.totalMoney(14)
print(s)
