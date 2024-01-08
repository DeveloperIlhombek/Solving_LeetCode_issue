class Solution:
    def countTriples(self, n: int) -> int:
        result=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                for x in range(1,n+1):
                    if x*x==j*j+i*i:
                        result+=1
        return result

print(Solution.countTriples(Solution,18))