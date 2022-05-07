original = sorted(input())
maybeAnagram = sorted(input())
isAnagram = True

for i, x in enumerate(original):
    if (maybeAnagram[i] != x):
        print("me enganei nao eh um anagrama")
        isAnagram = False

if (isAnagram):
    print("achei um anagrama")
