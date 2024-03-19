class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result=[]
        for i in range(left,right+1):
            length_of_number=len(str(i))
            count=0
            if i % 10 ==0:
                continue
            else:
                for j in range(length_of_number):
                    divided=str(i)[j]
                    if i % int(divided) ==0:
                        count += 1
                    else:
                        continue
                if length_of_number == count:
                    result.append(i)
        return result

print(Solution.selfDividingNumbers(Solution,47,85))
