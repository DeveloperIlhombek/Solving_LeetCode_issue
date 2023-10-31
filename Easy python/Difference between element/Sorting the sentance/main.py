class Solution:
    def sortSentence(self, s: str) -> str:
        answer=" "
        sp_str=s.split(" ")
        arr=[]
        for i in range(1,len(sp_str)+1):
            for j in sp_str:
                if str(i) in j:
                    arr.append(j[:-1])
        return answer.join(arr)

print(Solution.sortSentence(Solution, "Myself2 Me1 I4 and3"))




