# https://www.beecrowd.com.br/judge/pt/problems/view/1168

n = int(input())

ledsByValue = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
}

for _ in range(n):
    value = input()
    sum = 0

    for number in value:
        leds = ledsByValue[number]
        sum += leds
    print(str(sum) + " leds")
