class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l = []
        for char in s:
            if char in l:
                return char
            else:
                l.append(char)
