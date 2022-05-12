n = int(input())

for _ in range(n):
    firstText, secondText = input().split(" ")
    resultText = ""
    longestText = (firstText if len(firstText) >
                   len(secondText) else secondText)

    size = len(firstText)
    if (len(secondText) < len(firstText)):
        size = len(secondText)

    for i in range(size):
        resultText += firstText[i] + secondText[i]

    print(resultText + longestText[size:])
