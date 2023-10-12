class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        h=sorted(heights,reverse=True)
        result=[]
        for i in h:
            result.append(names[heights.index(i)])
        return result

print(Solution.sortPeople(Solution,["Alice","Bob","Bob"],[155,185,150]))