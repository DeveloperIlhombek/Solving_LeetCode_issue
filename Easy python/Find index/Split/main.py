class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        ans=[]
        for word in words:
            for i in word.split(separator):
                if i:
                    ans.append(i)

        return ans
print(Solution.splitWordsBySeparator(Solution,["$easy$","$problem$"],"$"))



