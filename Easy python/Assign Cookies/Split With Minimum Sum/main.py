class Solution:
    def splitNum(self, num: int) -> int:
        st = str(num)

        lt = []
        for i in st:
            lt.append(int(i))
        lt.sort()
        mx = ""
        mn = ""
        for i in range(len(lt)):
            if i % 2 == 0:
                mn += str(lt[i])
            else:
                mx += str(lt[i])
        return int(mx) + int(mn)

print(Solution.splitNum(Solution,4325))