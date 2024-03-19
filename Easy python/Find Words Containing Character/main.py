class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        result=[]
        for i in words:
            if x in i:
                result.append(words.index(i))
        return  result

print(Solution.findWordsContaining(Solution,["abc","bcd","aaaa","cbc"],"a"))
