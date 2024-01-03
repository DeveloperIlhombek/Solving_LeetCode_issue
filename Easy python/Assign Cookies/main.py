class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()  # Greed factorsni o'sish tartibida saralash
        s.sort()  # Pishiriq o'lchamlarini o'sish tartibida saralash

        content_children = 0
        i = 0  # Greed factors uchun indeks
        j = 0  # Pishiriq o'lchamlari uchun indeks

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_children += 1
                i += 1
            j += 1

        return content_children


# Namunaviy ishlatish:
greed_factors = [1,1,4,7]
cookie_sizes = [1, 1,5,8]
natija = Solution.findContentChildren(Solution, greed_factors, cookie_sizes)
print("Maksimal qoniqish bo'lgan bolalar soni:", natija)
