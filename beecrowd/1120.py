# https://www.beecrowd.com.br/judge/pt/problems/view/1120
while True:
    digit, value = input().split(" ")

    result = value.replace(digit, "")

    if (digit == "0" and value == "0"):
        break
    else:
        print(str(int(result)) if result != "" else "0")
