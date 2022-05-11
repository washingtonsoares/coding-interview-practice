while True:
    try:
        wordsLength, maxLinesPerPage, maxCharPerLine = map(
            int, input().split(" "))

        shortStory = input()

        lines = 0
        pages = 0
        words = shortStory.split(" ")
        currentIndex = 0

        while currentIndex < wordsLength:
            line = []
            lineSum = 0

            while currentIndex < wordsLength and (lineSum + len(words[currentIndex])) <= maxCharPerLine:
                wordWithSpace = words[currentIndex] + " "

                line.append(wordWithSpace)
                lineSum += len(wordWithSpace)
                currentIndex += 1
                currentIndex = currentIndex

            lines += 1
            if (lines >= maxLinesPerPage or currentIndex == wordsLength):
                lines = 0
                pages += 1

        print(pages)

    except EOFError:
        break
