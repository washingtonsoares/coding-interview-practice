# 27. Remove Element
# https://leetcode.com/problems/remove-element/

from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0

    for n in nums:
        if (n != val):
            nums[i] = n
            i += 1

    print(i)

    return i


removeElement([3, 2, 2, 3], 3)
