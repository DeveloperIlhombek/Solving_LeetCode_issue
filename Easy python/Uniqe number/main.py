class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        numberCount=[]
        for i in set(arr):
            numberCount.append(arr.count(i))
        if len(numberCount) == len(set(numberCount)):
            return True
        return False

print(Solution.uniqueOccurrences(Solution, [-3,0,1,-3,1,1,1,-3,10,0]))