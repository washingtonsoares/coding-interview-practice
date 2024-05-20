# O(n)
def findMaxK(nums):
    num_set = set(nums)
    max_k = -1

    for num in nums:
        if num > 0 and -num in num_set:
            max_k = max(max_k, num)

    print(num_set)
    return max_k

print(findMaxK([-1, 10, 6, 7, -7, 1]))

#  O(n*n)
def findMaxK2(nums):
        max = -1
        for n in nums:
            if n > max and -abs(n) in nums:
                max = n

        return max

        
        