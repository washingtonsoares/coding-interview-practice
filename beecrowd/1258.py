testCount = 0

while True:
    try:
        n = int(input())
        if (n == 0):
            break

        if (testCount > 0):
            print("")

        tShirtsToMake = []

        for i in range(n):
            name = input()
            color, size = input().split(" ")

            tShirtsToMake.append({"name": name, "color": color, "size": size})

        tShirtsToMake.sort(key=lambda item: (
            item['color'], -(ord(item['size'])), item['name']))

        for item in tShirtsToMake:
            print(item['color'] + " " + item['size'] + " " + item['name'])

        testCount += 1
    except EOFError:
        break
