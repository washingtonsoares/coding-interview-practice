from typing import List


def reverseString(s: List[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        left_temp = s[left]
        s[left] = s[right]
        s[right] = left_temp

        left += 1
        right -= 1

str_list = ["h","e","l","l","o"]
reverseString(str_list)
print(str_list)