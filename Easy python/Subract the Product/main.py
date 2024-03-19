class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multiple=1
        summa=0
        for i in list(str(n)):
            multiple *= int(i)
            print(multiple)
            summa += int(i)
            print(summa)
        return multiple-summa
print(Solution.subtractProductAndSum(Solution,4421))