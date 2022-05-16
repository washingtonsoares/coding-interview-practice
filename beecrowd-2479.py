n = int(input())
names = []
behavedWell = 0
behavedBad = 0

for i in range(n):
    behavior, name = input().split(" ")
    names.append(name)

    if (behavior == "+"):
        behavedWell += 1
    else:
        behavedBad += 1

for name in sorted(names):
    print(name)

print("Se comportaram: " + str(behavedWell) +
      " | Nao se comportaram: " + str(behavedBad))
