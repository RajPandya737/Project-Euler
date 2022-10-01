def gen_pentagon_numbers(n):
    nums = []
    for i in range(1, n+1):
        nums.append((i*(3*i-1))/2)
    return nums

def P(n):
    return (n*(3*n-1))/2

def binary_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

nums = gen_pentagon_numbers(500)

binary_search(nums, 1)

for j in range(1, 10000):
    for k in range(j, 10000):
        if binary_search(nums, P(k)-P(j)) is True and binary_search(nums, P(j)+P(k)) is True:
            print(k-j)