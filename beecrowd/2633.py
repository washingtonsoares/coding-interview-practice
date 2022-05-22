while True:
    try:
        n = int(input())
        meatAndDates = []

        for _ in range(n):
            meatAndDateStr = input()
            meatAndDates.append(meatAndDateStr)

        result = sorted(meatAndDates, key=lambda x: int(x.split(" ")[1]))

        for i, item in enumerate(result):
            end = " "
            if (i == n - 1):
                end = ""

            print(item.split(" ")[0], end=end)
        print("")
    except EOFError:
        break
