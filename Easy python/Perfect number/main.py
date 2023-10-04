class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return sum(i + num//i for i in range(1,int(num**0.5)+1) if num % i == 0) == 2*num if num != 1 else False

# return num in set([6,28,496,8128,33550336])☻
print(Solution.checkPerfectNumber(Solution,28))

