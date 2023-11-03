class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result=[]
        target_set=set(target)

        for i in range(1,target[-1]+1):
            if i in target_set:
                result.append("Push")
            else:
                result.append("Push")
                result.append("Pop")
        return result



print(Solution.buildArray(Solution,[1,3],3))


