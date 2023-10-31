class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        temp = ''
        count = 0
        for i in t:
            if count < len(s) and i == s[count]:
                temp += i
                count += 1
        if temp == s:
            return True
        else:
            return False


print(Solution.isSubsequence(Solution,"abc","abbac"))

