while True:
    try:
        text = input()
        shortcuts = []
        resultText = ""

        for i in range(len(text)):
            currentChar = text[i]
            if (currentChar == "_"):
                if (len(shortcuts) > 0 and shortcuts[-1] == "_"):
                    shortcuts.pop()
                    resultText += "</i>"
                else:
                    shortcuts.append("_")
                    resultText += "<i>"
            elif (currentChar == "*"):
                if (len(shortcuts) > 0 and shortcuts[-1] == "*"):
                    shortcuts.pop()
                    resultText += "</b>"
                else:
                    shortcuts.append("*")
                    resultText += "<b>"
            else:
                resultText += currentChar

        print(resultText)
    except EOFError:
        break
