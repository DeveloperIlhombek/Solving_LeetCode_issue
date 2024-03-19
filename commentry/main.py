# import nltk
# from nltk.tokenize import sent_tokenize
#
# # Sample comments
# comments = [
#     "User123: I really enjoyed this movie!",
#     "Admin: Thank you for your feedback.",
#     "User456: The service was terrible. I won't be coming back.",
#     "User123: @User456, I'm sorry you had a bad experience.",
#     "User789: Has anyone tried the new menu?",
#     "Admin: Yes, it's been getting good reviews.",
# ]
#
# # Tokenize comments into sentences
# sentences = [sent_tokenize(comment) for comment in comments]
#
# # Identify user commentary based on username patterns
# user_comments = []
# for sentence in sentences:
#     for s in sentence:
#         if s.startswith("User"):
#             user_comments.append(s)
# print(user_comments)
# # Separate user commentary from other content
# system_comments = [comment for comment in comments if comment not in user_comments]
#
# print("User Comments:")
# for comment in user_comments:
#     print(comment)
#
# print("\nSystem Comments:")
# for comment in system_comments:
#     print(comment)
# Maqola ma'lumotlari
maqola = {
    "Sifatli": [],
    "Salbiy": []
}

# Maqolaga bildirilgan sharhlar
sharhlar = [
    "Maqola juda yaxshi yozilgan deb ayta olmayman",
    "Shu maqolani o'qishdan ajoyib hisoblayman.",
    "Bu maqolani ko'rish juda qiyin deya olmayman.",
    "Men bu maqolani o'qib bo'lmadim.",
    "Maqola juda yaxshi yozilgan.",
    "Bu maqolani ko'rish juda qiyin ",
    "Men bu maqolani o'qib bo'lmadim."
]

# Sharhlar turlariga qarab ajratish
for sharh in sharhlar:
    if sharh.startswith("Ijobiy"):
        maqola["Sifatli"].append(sharh[9:])
    else:
        maqola["Salbiy"].append(sharh[9:])

# Natijalarni chop etish
print("Ijobiy Sharhlar:")
for sharh in maqola["Sifatli"]:
    print(sharh)

print("\nSalbiy Sharhlar:")
for sharh in maqola["Salbiy"]:
    print(sharh)
