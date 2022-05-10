n = int(input())
results = []

for x in range(n):
    value, actual, convertTo = input().split(" ")
    valueAsNumber = int(value)

    if (valueAsNumber < -1000 or valueAsNumber > 1000):
        results.append("Valores invalidos")
        continue

    if (actual == 'C' and convertTo == 'K'):
        results.append(valueAsNumber + 273.15)
    elif (actual == 'K' and convertTo == 'C'):
        results.append(valueAsNumber - 273.15)
    elif (actual == 'C' and convertTo == 'F'):
        results.append(valueAsNumber * (9/5) + 32)
    elif (actual == 'F' and convertTo == 'C'):
        results.append((valueAsNumber - 32) * 5/9)
    elif (actual == 'F' and convertTo == 'K'):
        results.append((valueAsNumber - 32) * 5/9 + 273.15)
    elif (actual == 'K' and convertTo == 'F'):
        results.append((valueAsNumber - 273.15) * 9/5 + 32)
    else:
        results.append("Valores invalidos")

for item in results:
    if isinstance(item, str):
        print(item)
    else:
        print("{:.2f}".format(item))
