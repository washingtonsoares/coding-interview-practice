symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

sum = 0
romanStr = "MCMXCIV"
lenRoman = len(romanStr)

for i, char in enumerate(romanStr):
    value = symbols[char]

    if (i + 1 < lenRoman and symbols[romanStr[i]] < symbols[romanStr[i + 1]]):
        sum -= value
    else:
        sum += value

print(sum)
