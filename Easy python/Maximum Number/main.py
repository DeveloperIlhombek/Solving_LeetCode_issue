class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        result=[]
        for i in sentences:
            words=i.split(" ")
            result.append(len(words))
        return max(result)


print(Solution.mostWordsFound(Solution,["please wait", "continue to fight", "continue to win"]))

