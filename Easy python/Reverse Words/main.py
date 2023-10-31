class Solution:
    def reverseWords(self, s: str) -> str:
        result=[]
        for i in list(s.split(" ")):
            result.append(i[::-1])
        return " ".join(result)


print(Solution.reverseWords(Solution, "Let's take LeetCode contest"))
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(map(lambda word: word[::-1], s.split()))

