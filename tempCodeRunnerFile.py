for j in range(1, 10000):
    for k in range(j+1, 10000):
        if binary_search(nums, P(j)-P(k)) is True and binary_search(nums, P(j)+P(k)) is True:
            print(k-j)