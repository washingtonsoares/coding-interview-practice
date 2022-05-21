n, k = map(int, input().split(" "))
names = []

for i in range(n):
    names.append(input())

for index, name in enumerate(sorted(names)):
    if (index + 1 == k):
        print(name)
