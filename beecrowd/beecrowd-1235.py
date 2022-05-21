n = int(input())

for _ in range(n):
    text = input()

    first_half = text[:len(text)//2]
    second_half = text[len(text)//2:]

    print(first_half[::-1] + second_half[::-1])
