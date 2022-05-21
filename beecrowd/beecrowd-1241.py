# https://www.beecrowd.com.br/judge/pt/problems/view/1241

n = int(input())

for _ in range(n):
    x, y = input().split(" ")
    print("encaixa" if x.endswith(y) else "nao encaixa")
