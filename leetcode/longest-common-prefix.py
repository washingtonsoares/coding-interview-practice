# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
strs = ["flower", "flow", "flight"]

strs.sort(key=len)

firstStr = strs[0]

longestStr = ""

for i in range(len(firstStr)):
    currentStr = firstStr[i]
    startswithStr = True

    for str in strs[1:]:
        if (not str[i:].startswith(currentStr)):
            startswithStr = False
            break

    if (startswithStr):
        longestStr += currentStr
    else:
        break

print(longestStr)
