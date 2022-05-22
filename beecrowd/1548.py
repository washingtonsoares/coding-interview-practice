n = int(input())

for i in range(n):
    m = int(input())
    grades = None
    result = 0

    grades = list(map(int, input().split(" ")))

    for index, grade in enumerate(sorted(grades, reverse=True)):
        if (grade == grades[index]):
            result += 1

    print(result)
