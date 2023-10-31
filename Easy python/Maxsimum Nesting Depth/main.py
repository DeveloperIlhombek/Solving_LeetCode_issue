class Solution:
    def maxDepth(self, s: str) -> int:
        arr=list(s)
        max=0
        count=0
        for i in arr:
            if i == "(" or i==")":
                if i=="(":
                    count +=1;
                    max=count  if max<count else  max
                else:
                    count-=1
        return max

print(Solution.maxDepth(Solution,"((2+((2))"))


