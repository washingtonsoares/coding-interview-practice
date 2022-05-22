while True:
    try:
        n, m = map(int, input().split(" "))

        scores = []

        for i in range(n):
            scores.append(int(input()))

        scores.sort(reverse=True)

        for i in range(m):
            p = int(input())

            print(scores[p-1])

    except EOFError:
        break
