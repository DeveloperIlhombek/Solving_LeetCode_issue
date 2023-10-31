class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if '1' not in  list(s):
            return s
        if '1' in list(s):
            son = sorted(list(s))
            son.reverse()
            son.remove("1")
            son.append('1')
            return "".join(son)


print(Solution.maximumOddBinaryNumber(Solution,"0010"))




