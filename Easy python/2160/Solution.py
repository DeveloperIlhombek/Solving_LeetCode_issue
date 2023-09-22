class Solution:
    def minimumsum(self, num: int) -> int:
        s=sorted(str(num))
        return int( s[0]+s[2])+int(s[1]+s[3])

num=2932
print(Solution.minimumsum(Solution,num))