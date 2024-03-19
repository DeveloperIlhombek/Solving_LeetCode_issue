class Solution:
    def countSeniors(self, details: list[str]) -> int:

        # "  7868190130  M 75 22"
        age=0
        for i in details:
            if int(i[11:13])>60:
                age+=1
        return age
answer=Solution()
x=answer.countSeniors(["7868190130M6522","5303914400F6211","9273338290F5010"])
print(x)