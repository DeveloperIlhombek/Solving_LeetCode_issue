class Solution:  # Mening yechimimda xatolik bor
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            x=haystack.partition(needle)
            res=list(x)
            if haystack.startswith(needle):
                indeks = res.index(needle)-1
            else:
                indeks=res.index(needle)
        else:
            indeks = -1
        return indeks



print(Solution.strStr(Solution,"sadbutsad","but"))