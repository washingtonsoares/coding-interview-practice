# https://www.beecrowd.com.br/judge/pt/problems/view/1024

n = int(input())

for _ in range(n):
    text = input()

    text2 = ""
    # first step
    for char in text:
        if (char.isalpha()):
            text2 += chr(ord(char) + 3)
        else:
            text2 += char
    # second step
    text3 = text2[::-1]
    # third step
    text4 = ""

    first_half = text3[:len(text3)//2]
    second_half = text3[len(text3)//2:]

    for char in second_half:
        text4 += chr(ord(char) - 1)

    print(first_half, end='')
    print(text4)
