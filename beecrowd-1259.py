n = int(input())
odd = []
even = []

for _ in range(n):
    number = int(input())

    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

for n in sorted(even):
    print(n)

for n in sorted(odd, reverse=True):
    print(n)
