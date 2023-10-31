class Solution:
    def finalString(self, s: str) -> str:
        res=[]
        for i in s:
            if i !="i":
                res.append(i)
            elif i =="i":
                res.reverse()
        return "".join(res)

print(Solution.finalString(Solution,"poiinter"))

