# using a "two pointers" like approach
def isPalindrome1(x):
    numberAsStr = str(x)
    strLen = len(numberAsStr)

    for index, num in enumerate(range(strLen)):
        if numberAsStr[index] != numberAsStr[strLen - index - 1]:
            return False
    
    return True

print(isPalindrome1(1221))

# using a more python-like approach
def isPalindrome2(x):
    return str(x) == str(x)[::-1]