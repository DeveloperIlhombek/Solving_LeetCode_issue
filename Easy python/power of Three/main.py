class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count=0
        for i in words:
            for j in i:
                if j in allowed:



# print(Solution.countConsistentStrings(Solution,"abc", ["a","b","c","ab","ac","bc","abc"]))



