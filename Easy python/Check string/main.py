class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        ans=""
        for word in words:
            ans+=word[0]

        return ans==s