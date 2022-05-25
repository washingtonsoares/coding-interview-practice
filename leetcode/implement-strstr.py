# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/

def strStr(haystack: str, needle: str) -> int:
    if not needle in haystack:
        return -1
    print(haystack[:len(haystack) + 10000])


strStr("hello", "")

# def strStr(haystack: str, needle: str) -> int:
#     if not needle:
#         return 0

#     if len(needle) > len(haystack):
#         return -1

#     for index, h in enumerate(haystack):
#         if (h == needle[0] and len(haystack) - index >= len(needle)):
#             auxIndex = index + 1
#             flag = True
#             for n in needle[1:]:
#                 if (n != haystack[auxIndex]):
#                     flag = False
#                     break
#                 else:
#                     auxIndex += 1

#             if (flag == True):
#                 return index

#     return -1
