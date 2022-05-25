# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target < nums[0]:
        return 0

    if target > nums[-1]:
        return len(nums)

    for i, n in enumerate(nums):
        if (n == target):
            return i
        elif (n > target):
            return i


print(searchInsert([1, 3], 2))
