while True:
    try:
        text1 = input()
        text2 = input()
        aux = ""

        if (len(text2) < len(text1)):
            aux = text1
            text1 = text2
            text2 = aux

        maxSubStr = 0

        if (text1 in text2):
            print(len(text1))
        else:
            for i in range(len(text1)):
                subStr = ""
                for j in range(i, len(text1)):
                    subStr += text1[j]

                    if (subStr in text2):
                        if (len(subStr) > maxSubStr):
                            maxSubStr = len(subStr)

            print(maxSubStr)

    except EOFError:
        break
