class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        add=[]
        for i in range(len(grid)):
            for j in grid[i]:
                add.append(j)
        result=[]
        for i in range(1,len(grid)**2+1):
            if add.count(i)==2:
                result.append(i)
        for i in range(1,len(grid)**2+1):
            if i not in add:
                result.append(i)
        return result
print(Solution.findMissingAndRepeatedValues(Solution,     [[1,3],[2,2]]))

