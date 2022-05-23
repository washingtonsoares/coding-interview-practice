def isValid(strs: str) -> bool:
    stack = []
    symbols = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    for s in strs:
        if (s in symbols):
            if (stack and symbols[s] == stack[-1]):
                stack.pop()
            else:
                return False
        else:
            stack.append(s)

    return True if stack == [] else False


print(isValid("([]){"))
# def isValid(strs: str) -> bool:
#     stack = []
#     result = False

#     for s in strs:
#         if (s in ["{", "[", "("]):
#             stack.append(s)
#         else:
#             if (len(stack) == 0):
#                 return False
#             if (s == "]" and stack[-1] == "["):
#                 stack.pop()
#                 result = True
#             elif (s == "}" and stack[-1] == "{"):
#                 stack.pop()
#                 result = True
#             elif (s == ")" and stack[-1] == "("):
#                 stack.pop()
#                 result = True
#             else:
#                 result = False
#                 break

#     if (len(stack) > 0):
#         return False

#     return result
