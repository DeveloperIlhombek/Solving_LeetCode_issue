class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovel=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        len_s=int(len(s)/2)
        a=s[0:len_s:]
        b=s[len_s::]
        a_count,b_count=0,0
        for i in a:
            if i in vovel:
                a_count+=1

        for i in b:
            if i in vovel:
                b_count+=1
        return a_count==b_count

print(Solution.halvesAreAlike(Solution,"textbook"))
