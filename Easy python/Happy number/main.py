class Solution:
    def isHappy(self, n: int) -> bool:
        flag=True
        while flag:
            numbers=[]
            for i in str(n):
                numbers.append((int(i))**2)
            number_sum=sum(numbers)
            n=number_sum
            cell_number=len(str(n))
            if cell_number==1:
                flag=False
        return n==1

solution=Solution()
x=solution.isHappy(19)
print(x)