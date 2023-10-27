class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for i in operations:
            if i =="D":
                stack.append(2*stack[-1])
            elif i=="C":
                stack.pop()
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return stack



print(Solution.calPoints(Solution,["5","2","C","D","+"]))


